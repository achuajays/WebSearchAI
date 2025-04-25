
import React, { useState, useRef, useEffect } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';
import { useToast } from '@/components/ui/use-toast';
import { Loader2 } from 'lucide-react';

interface Message {
  text: string;
  isBot: boolean;
}

const ChatContainer = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const { toast } = useToast();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (message: string) => {
    try {
      setIsLoading(true);
      // Add user message
      setMessages(prev => [...prev, { text: message, isBot: false }]);

      // Make API call
      const response = await fetch('https://websearchai-production.up.railway.app/api/research/run', {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: message }),
      });

      const data = await response.json();
      
      // Add bot response
      setMessages(prev => [...prev, { 
        text: data.research_data || "No data found",
        isBot: true 
      }]);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to get response. Please try again.",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[70vh] mx-auto max-w-3xl bg-white/80 backdrop-blur-sm rounded-xl shadow-lg border-2">
      <div className="flex-1 overflow-y-auto p-6 relative">
        {messages.length === 0 && (
          <div className="flex items-center justify-center h-full text-gray-500">
            <p>Start your research by asking a question</p>
          </div>
        )}
        {messages.map((message, index) => (
          <ChatMessage
            key={index}
            message={message.text}
            isBot={message.isBot}
          />
        ))}
        {isLoading && (
          <div className="absolute inset-0 flex items-center justify-center bg-white/70 backdrop-blur-sm z-10">
            <Loader2 className="h-10 w-10 animate-spin text-blue-500" />
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <ChatInput onSend={handleSendMessage} isLoading={isLoading} />
    </div>
  );
};

export default ChatContainer;
