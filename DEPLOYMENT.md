# 🚀 Deploy Your Titanic Survival Predictor

This guide will help you deploy your Titanic Survival Predictor web app to free hosting platforms.

## 🌟 **Option 1: Railway (Recommended)**

Railway offers the best free tier for Python apps with easy GitHub integration.

### **Free Tier Benefits:**
- ✅ 500 hours/month (about 16-17 hours/day)
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Easy GitHub integration

### **Deploy to Railway:**

1. **Create a GitHub Repository:**
   ```bash
   # Initialize git in your project directory
   git init
   git add .
   git commit -m "Initial commit: Titanic Survival Predictor"
   
   # Create a new repository on GitHub and push
   git remote add origin https://github.com/YOUR_USERNAME/titanic-predictor.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy to Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect it's a Python app and deploy it!

3. **Your app will be live at:** `https://your-app-name.up.railway.app`

---

## 🌟 **Option 2: Render**

Render is another excellent free hosting platform.

### **Free Tier Benefits:**
- ✅ 750 hours/month
- ✅ Automatic HTTPS
- ✅ Custom domains

### **Deploy to Render:**

1. **Push to GitHub** (same as above)

2. **Deploy to Render:**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python app.py`
   - Click "Create Web Service"

---

## 🌟 **Option 3: PythonAnywhere**

Great for Python-specific hosting with a generous free tier.

### **Free Tier Benefits:**
- ✅ Always-on web app
- ✅ 3 months free, then limited but still free
- ✅ Python-optimized environment

### **Deploy to PythonAnywhere:**

1. **Sign up at [pythonanywhere.com](https://pythonanywhere.com)**

2. **Upload your files:**
   - Use the file manager to upload your project
   - Or clone from GitHub in the console

3. **Configure web app:**
   - Go to "Web" tab
   - Create new web app
   - Choose Flask
   - Point to your `app.py` file

---

## 🌟 **Option 4: Vercel (Serverless)**

Good for serverless deployment.

### **Deploy to Vercel:**

1. **Create `vercel.json`:**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

2. **Deploy:**
   - Install Vercel CLI: `npm i -g vercel`
   - Run: `vercel --prod`

---

## 📋 **Deployment Files Included**

Your project now includes these deployment files:

- **`Procfile`** - Tells hosting platforms how to run your app
- **`railway.json`** - Railway-specific configuration
- **`runtime.txt`** - Specifies Python version
- **`requirements.txt`** - Your Python dependencies

## 🔧 **Pre-Deployment Checklist**

✅ All files committed to git  
✅ requirements.txt up to date  
✅ App runs locally with `python app.py`  
✅ GitHub repository created  
✅ Deployment files included  

## 🌐 **Post-Deployment**

Once deployed, your Titanic Survival Predictor will be accessible worldwide at your hosting URL!

**Example URLs:**
- Railway: `https://titanic-predictor.up.railway.app`
- Render: `https://titanic-predictor.onrender.com`
- Vercel: `https://titanic-predictor.vercel.app`

## 🎯 **Recommended Choice**

**Use Railway** for the best experience:
- Fastest deployment
- Best free tier
- Excellent performance
- Easy custom domains

## ⚡ **Quick Start (Railway)**

```bash
# 1. Push to GitHub
git init && git add . && git commit -m "Deploy Titanic Predictor"

# 2. Go to railway.app
# 3. Click "Deploy from GitHub"
# 4. Select your repo
# 5. Your app is live! 🎉
```

---

**🎉 Congratulations! Your Titanic Survival Predictor is now live and accessible to anyone in the world!**