import React from "react";
import NavBar from "../components/NavBar";

const MainLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <>
      <header>
        <NavBar />
      </header>
      <main>{children}</main>
      <footer>
        <p className="text-center text-base text-bold">
          Copyrights &copy; reserved by Gopal Khadka - 2024
        </p>
      </footer>
    </>
  );
};

export default MainLayout;
