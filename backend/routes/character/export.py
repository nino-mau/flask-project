from flask import Blueprint, request, jsonify
from flask import current_app as app
from playwright.async_api import async_playwright
from services.cloudinary import CloudinaryService
from io import BytesIO

export_bp = Blueprint("export_bp", __name__)


@export_bp.get("")
async def get_screenshot():
    character_id = request.args.get("character_id")
    app.logger.info(character_id)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(
            f"http://frontend:3000/character/{character_id}", wait_until="networkidle"
        )

        element = page.locator(".card_character")
        screenshot = await page.locator(".card_character").screenshot(
            type="png", omit_background=False
        )

        await browser.close()

        cloudinary = CloudinaryService()

        upload_result = cloudinary.upload(BytesIO(screenshot))

        app.logger.info(upload_result)

        return jsonify({"msg": "success", "image_hash": upload_result["url"]}), 200
