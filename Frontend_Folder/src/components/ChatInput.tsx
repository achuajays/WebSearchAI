
import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { MessageSquare, Loader2 } from 'lucide-react';

interface ChatInputProps {
  onSend: (message: string) => void;
  isLoading: boolean;
}

const ChatInput = ({ onSend, isLoading }: ChatInputProps) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim()) {
      onSend(message);
      setMessage('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 p-4 border-t">
      <Input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your query..."
        disabled={isLoading}
        className="flex-1"
      />
      <Button type="submit" disabled={isLoading || !message.trim()}>
        {isLoading ? (
          <Loader2 className="h-5 w-5 animate-spin" />
        ) : (
          <MessageSquare className="h-5 w-5" />
        )}
        <span className="ml-2">{isLoading ? 'Loading...' : 'Send'}</span>
      </Button>
    </form>
  );
};

export default ChatInput;
