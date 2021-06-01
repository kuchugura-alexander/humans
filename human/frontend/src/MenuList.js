import { Link } from 'react-router-dom'

function MenuList(){
    return (
        <div  className="humans--list">
            <table  className="table">
                <thead  key="thead">
                    <tr>
                        <th>#</th>
                        <th>Function</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr  key="h">
                        <td>0</td>
                        <td>
                            <Link to="/human/" className="btn btn-primary">Humans</Link>
                        </td>
                        <td>
                            <Link to='/human/'>
                                <button type="button" className="btn btn-info">Desc</button>
                            </Link>
                        </td>
                        <td></td>
                    </tr>
                    <tr  key="g">
                        <td>1</td>
                        <td>
                            <Link to="/gender/" className="btn btn-primary">Genders</Link>
                        </td>
                        <td>
                            <Link to='/gender/'>
                                <button type="button" className="btn btn-info">Desc</button>
                            </Link>
                        </td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

export  default  MenuList;


