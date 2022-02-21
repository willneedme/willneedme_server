import React, { useEffect, useRef, useState} from "react";
// import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import {useMediaQuery} from 'react-responsive';
import "../../css/header.css";

const Header = (props) => {
    const [menuToggle, setMenuToggle] = useState(false);
    const isMobile = useMediaQuery({
        query : "(max-width:768px)"
    });
    const mobileMenu = useRef();
    const publicUrl = process.env.PUBLIC_URL;

    const menuList = [
        { name: '주식', address: "/korea" },
        { name: '해외주식', address: "/international" },
    ];

    const mobileToggle = () => {
        if (isMobile&&menuToggle) {
            mobileMenu.current.style = "display:none"
            setMenuToggle(false);
        }
        if (isMobile&&!menuToggle) {
            mobileMenu.current.style = "display:block"
            setMenuToggle(true)
        }
    }

    useEffect(() => {
        if(!isMobile) mobileMenu.current.style = "display:none"
    } , [isMobile])

    return (
        <>
            <nav className = "navbar">
                <div className = {"navbar_title"}>
                    <a href = "http://willneedme.com">Willneedme</a>
                </div>
                <ul
                    className={!isMobile ? "navbar_menu" : "navbar_hidden"}
                >
                    {menuList.map((data) => (
                        <li
                            data={data.data}
                            key={ data.address}
                        >
                            {data.name}
                        </li>
                    ))}
                </ul>
                {isMobile ? <div className="navbar_link" onClick={mobileToggle}>
                    <img
                        src={`${publicUrl}/menu_icon.png`}
                    />
                </div> : <div className="login">로그인</div>}
            </nav>
            <ul
                ref={mobileMenu}
                className={isMobile ? "navbar_menu_mobile" : "navbar_hidden"}
            >
                {menuList.map((data) => (
                    <li
                        data={data.data}
                        key={ data.address}
                    >
                        {data.name}
                    </li>
                ))}
            </ul>
        </>        
    );
}

const stateToProps = (state) => {
    return {};
}

const dispatchToProps = (dispatch) => {
    return {};
}

export default connect(stateToProps , dispatchToProps)(Header);