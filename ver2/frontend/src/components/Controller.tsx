import React, { useState } from 'react'
import Title from './Title';

function Controller() {

    const [isLoading, setIsLoading] = useState(false);
    const [messages, setMessages] = useState<any[]>([]);

    const createBlobURL = (data: any) => {};
    const handleStop = async () => {};


 
    return ( 
        <div className='h-screen overflow-y-hidden'>
            <Title setMessages={setMessages}></Title>
            <div className='flex flex-col justify-between h-full overflow-y-scroll pb-96'>
                Peepee Poopoo
            </div> 
        </div>
    );
}

export default Controller