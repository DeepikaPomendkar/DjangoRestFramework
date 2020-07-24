import React from 'react'
import {useForm, appendErrors} from 'react-hook-form'
import { useState } from 'react';


export default function Loginbox() {

    const [errorMsg, setErrorMsg] = useState('')

    const {register,handleSubmit,errors}=useForm()

    const onSubmit=(data)=>{
        var isError=0
        var re = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/
        if(!re.test(data.email)){
            setErrorMsg('*Incorrect Email')
            isError=1
        }
        if(!(data.pass===data.rpass)){
            setErrorMsg('*Passwords do not match')
            isError=1
        }
        if(isError==0){
            setErrorMsg('')
            console.log(data)
        }
        
    }

    return (
        <div class='loginbox'>
            <p class='boxtitle'>Sign Up</p>
                <form onSubmit={handleSubmit(onSubmit)} autoComplete='off'>
                    <input type='text' name='name' class='linput' placeholder='Enter Name' ref={register({required:true})} />
                    <br/>
                    <input type='text' name='email' class='linput' placeholder='Enter Email' ref={register({required:true})} />
                    <br/>
                    <input type='text' name='pno' class='linput' placeholder='Enter Phone Number' ref={register({required:true})} />
                    <br/>
                    <input type='password' name='pass' class='linput' placeholder='Enter Password' ref={register({required:true,minLength:{value:8,message:'*Password too short'}})} />
                    <br/>
                    <input type='password' name='rpass' class='linput' placeholder='Re-enter Password' ref={register({required:true})} />
                    <br/>
                    {errors.pass && <p class='errormsg'>{errors.pass.message}</p>}
                    <p class='errormsg'>{errorMsg}</p>
                    <input type='Submit' class='lbtn' value='Sign Up'/>
                </form>
        </div>
    )
}

