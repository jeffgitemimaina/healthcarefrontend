﻿## Deployment on Render
1. **Push to GitHub**:
   - Ensure all files are committed and pushed to a GitHub repository.
2. **Create Render Web Service**:
   - Go to [Render](https://render.com), click **New > Web Service**.
   - Connect your GitHub repository.
   - Configure:
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
     - Environment Variable: `BACKEND_API_URL=https://healthcare-api-backend.onrender.com/api`
3. **Access the App**:
   - After deployment, visit  `https://healthcarefrontend-fwaf.onrender.com
4. **Update Backend URL**:
   - Update `templates/index.html` with the correct backend URL and redeploy.
5. Link to the prototype and the powerpoint presentation [google drive](https://drive.google.com/drive/folders/1_NpFjaUNCHUUZNsjSmSv1ZpWJJf7i3Ok?usp=sharing) 
