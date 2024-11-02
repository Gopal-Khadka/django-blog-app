import React, { useState } from "react";
import Button from "./Button";

const NavBar: React.FC = () => {
  // State to manage the mobile menu visibility
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Toggle function for mobile menu
  const handleNavBar = () => {
    setIsMenuOpen((prev) => !prev);
  };

  return (
    <nav className="bg-slate-600 flex flex-col md:flex-row px-3 py-2 items-center fixed top-0 w-full">
      <div className="font-semibold text-2xl tracking-wide w-1/3">
        DesiBlogs
      </div>
      <section id="menus" className="flex justify-between flex-grow flex-col md:flex-row gap-2 items-center">
        <ul
          id="links"
          className={`cursor-pointer md:flex ${
            isMenuOpen ? "flex" : "hidden"
          } gap-2 flex-wrap`}
        >
          <li>Home</li>
          <li>About</li>
          <li>Posts</li>
          <li>Forum</li>
          <li>Contact</li>
        </ul>

        {/* Auth Button for large and small screens */}
        <div
          id="auth-btn"
          className={`${
            isMenuOpen ? "block" : "hidden"
          } md:block cursor-pointer`}
        >
          <Button text="Login/SignUp" />
        </div>
      </section>

      {/* Hamburger Menu Icon for small screens */}
      <div className="md:hidden cursor-pointer">
        <button onClick={handleNavBar}>&#8801;</button>
      </div>
    </nav>
  );
};

export default NavBar;
