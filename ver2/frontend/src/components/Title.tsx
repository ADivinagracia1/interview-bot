import { useState } from 'react';
import axios from 'axios';

type Props = {
    setMessages: any;
};

function Title({ setMessages }: Props) {

    const [isResetting, setIsResetting] = useState(false);

    // Reset the conversation
    const resetConversation = async () => {
        setIsResetting(true);   // Start resetting

        await axios.get("http://localhost:8000/reset").then((res) => {
            if (res.status == 200) {
                setMessages([])
            } else {
                console.error("There was an error with the API request to the back end")
            }
        }).catch((err) => {
            console.error(err.message)
        })

        setIsResetting(false);  // Finish resetting
    }

    return (
        <div>
            <button onClick={resetConversation} className='bg-indigo-500 p-5'>RESET</button>
        </div>
    )
}

export default Title