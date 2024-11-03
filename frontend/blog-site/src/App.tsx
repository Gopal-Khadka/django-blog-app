import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Forum from "./pages/Forum";
import Posts from "./pages/Posts";
import About from "./pages/About";
import Contact from "./pages/Contact";
import MainLayout from "./layouts/MainLayout";
import Login from "./features/auth/Login";

function App() {
  const routes = [
    { path: "/", element: <Home /> },
    { path: "/about", element: <About /> },
    { path: "/contact", element: <Contact /> },
    { path: "/forum", element: <Forum /> },
    { path: "/posts", element: <Posts /> },
    { path: "/auth", element: <Login /> },
  ];

  return (
    <Router>
      <Routes>
        {routes.map(({ path, element }) => (
          <Route
            key={path}
            path={path}
            element={<MainLayout>{element}</MainLayout>}
          />
        ))}
      </Routes>
    </Router>
  );
}

export default App;
