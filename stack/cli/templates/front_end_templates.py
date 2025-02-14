

#

VITE_CONFIG = """
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: true,
    port: 3000
  }
})
"""
TAILWIND_CONFIG_JS = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}"""


POST_CSS_CONFIG = """
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""


PACKAGE_JSON = """
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.20",
    "postcss": "^8.5.1",
    "tailwindcss": "^3.4.17",
    "vite": "^5.0.0"
  }
}

"""

INDEX_CSS_CONFIG = """
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vanilla:hover {
  filter: drop-shadow(0 0 2em #f7df1eaa);
}


button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
}
"""

TEMPLATES = {
    'vite.config.js':VITE_CONFIG,
    'tailwind.config.js':TAILWIND_CONFIG_JS,
    'postcss.config.js':POST_CSS_CONFIG,
    'index.css':INDEX_CSS_CONFIG,
    'package.json':PACKAGE_JSON
}



################################################
# client_side_routing 
################################################


INDEX_HTML = """




"""

ROUTER_JS = """
const Router = {
    init: () => {
        console.log("Router: running");
        document.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', e => {
                e.preventDefault();
                const url = e.target.getAttribute("href");
                // Fix: Changed Router.nav.url to Router.nav(url)
                Router.nav(url);
            });
        });
        // Add popstate event listener to handle browser back/forward
        window.addEventListener('popstate', e => {
            if (e.state && e.state.router) {
                Router.nav(window.location.pathname, false);
            }
        });
    },
    nav: async (route, addToHistory = true) => {
        console.log("Navigation triggered to:", route);
        if (addToHistory) {
            history.pushState({ router: true }, null, route);
        }
        // Here you can add logic to update your page content based on the route
        // For example:
        switch (route) {
            case '/home':
                // Update content for home page
                break;
            case '/blog':
                // add content here 
                break;
            case '/projects':
                // Update content for projects page
                break;
            case '/contact':
                // Update content for contact page
                break;
            default:
                console.log('Route not found');
        }
    }
};

export default Router;
"""

MAIN_JS = """



"""

Frontend_files_to_delete = {
   #'src':['main.js'],
   'public':['vite.svg']
}


FRONTEND_FILES = {
    'src':['router.js']
}


TEMPLATES_ROUTING = {
  'main.js':MAIN_JS,
  'router.js':ROUTER_JS,
  'index.html':INDEX_HTML
}