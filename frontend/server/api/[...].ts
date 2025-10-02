import { defineEventHandler, proxyRequest, getRequestURL } from 'h3';

export default defineEventHandler(async (event) => {
  const url = getRequestURL(event);
  const targetUrl = `http://backend:5000${url.pathname}${url.search}`;
  return proxyRequest(event, targetUrl);
});
