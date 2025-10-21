import { defineEventHandler, proxyRequest, getRequestURL } from 'h3';

export default defineEventHandler(async (event) => {
  const rs = useRuntimeConfig();
  const url = getRequestURL(event);
  const targetUrl = `${rs.public.apiBase}${url.pathname}${url.search}`;
  return proxyRequest(event, targetUrl);
});
