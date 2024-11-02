import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Forum from "./pages/Forum";
import Posts from "./pages/Posts";
import About from "./pages/About";
import Contact from "./pages/Contact";
import MainLayout from "./layouts/MainLayout";
import Login from "./features/auth/Login";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainLayout children={<Home />} />} />
        <Route path="/about" element={<MainLayout children={<About />} />} />
        <Route
          path="/contact"
          element={<MainLayout children={<Contact />} />}
        />
        <Route path="/forum" element={<MainLayout children={<Forum />} />} />
        <Route path="/posts" element={<MainLayout children={<Posts />} />} />
        <Route path="/auth" element={<MainLayout children={<Login />} />} />
      </Routes>
    </Router>
  );
}

export default App;
