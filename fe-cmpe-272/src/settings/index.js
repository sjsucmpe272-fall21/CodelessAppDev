const CMPE_272_FLASK_API =
  process.env.REACT_APP_API_BASE_URL || "http://localhost:5000";

export const GITHUB_LOGIN_URL = `${CMPE_272_FLASK_API}/login`;
export default CMPE_272_FLASK_API;
