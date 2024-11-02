import React from "react";
import NavBar from "../components/NavBar";

const MainLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <div className="bg-slate-950 text-white">
      <header>
        <NavBar />
      </header>
      <main>{children}</main>
      <footer>
        <p>2024 My Website Footer</p>
      </footer>
    </div>
  );
};

export default MainLayout;
