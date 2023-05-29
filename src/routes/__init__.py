from src.routes import health_check, user, auth

routers = [health_check.router, user.router, auth.router]
