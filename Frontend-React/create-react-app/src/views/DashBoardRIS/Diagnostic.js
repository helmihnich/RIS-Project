import React from 'react';
import { useParams } from 'react-router-dom';
 import irmImage from './assets/images.png';
import "./Diagnostic.css";

const Diagnostic = () => {
    const { patientName } = useParams();
    return (
        <div>
            <div className='up-text d-flex align-items-center'>
                <p>Dashboard / My patient / <span>Diagnostic</span></p>
                <hr className="breadcrumb-line" />
            </div>
            <div className="row justify-content-end">
                <div className="col-auto">
                    <button className="mb-2 delete-button">
                        <span>Delete the examination</span>
                    </button>
                </div>
            </div>
            <div className="container">
                <div className="row">
                    {/* Column for patient details */}
                    <div className="card p-3 mb-3 align-items-center justify-content-center text-align-center">
                    <div className='details'>
                        <p className="mb-1">Name: <span>{patientName}</span></p>
                        <p className="mb-1">Date: <span>20/12/2020</span></p>
                        <p className="mb-1">Type: <span>Thorax Examination</span></p>
                    </div>
                    <div className='breadcrumb-line mb-5 w-75'></div> 
                    <div className='row justify-content-center'>
                        <img src={irmImage} alt="User Icon" className="mmt-4 col-md-5" />
                        <div className="diagnosis d-flex flex-column col-md-6 ">
                            <p className='fs-3'>Diagnostic</p>
                            <div className='breadcrumb-line mb-5 w-100'></div> 
                                <span>To diagnose lung disease, your physician will listen to you breathe with a stethoscope. If pneumothorax or atelectasis is suspected, no breathing sounds will be apparent as you inhale and exhale.</span>
                            </div>
                    </div>
 
                </div>

                    
                </div>
            </div>
        </div>
    );
};

export default Diagnostic;
