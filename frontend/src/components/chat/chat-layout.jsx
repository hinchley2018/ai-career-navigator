import useMediaQuery from '@mui/material/useMediaQuery';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import ChatDialog from './chat-dialog';
export default function ChatLayout(){
    return (
        <Box sx={{ display: 'flex', minHeight: '100vh' }}>
            <CssBaseline />
            <Box sx={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                {/* <Header1 onDrawerToggle={handleDrawerToggle} /> */}
                <ChatDialog />
            </Box>
        </Box>
    )
}