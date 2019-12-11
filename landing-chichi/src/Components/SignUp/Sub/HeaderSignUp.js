import React, {Component} from 'react';
import {Link} from "react-scroll/modules";

class HeaderSignUp extends Component {
    render() {
        return (
            <div className='w-100 pl-sm-2 pr-sm-2'>
                <ul className='d-flex col-sm-10 col-md-8 justify-content-between p-0'>
                    <li className='list-unstyled'><a href=" " className='alink fs-13vw'>خانه</a></li>
                    <li className='  list-unstyled'><a href=" " className='alink fs-13vw'>درباره ما</a></li>
                    <li className='  list-unstyled'>
                        <Link name="first" activeClass="active" className="    w-100 pointer " to="SignUp" spy={true} smooth={true} duration={500}  ><a href=' ' className='alink fs-13vw'>ثبت نام </a> </Link>
                    </li>
                </ul>
            </div>
        );
    }
}

export default HeaderSignUp;