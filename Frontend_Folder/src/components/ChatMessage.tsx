
import React from 'react';
import { cn } from '@/lib/utils';
import { Bot, User } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

interface ChatMessageProps {
  message: string;
  isBot: boolean;
}

const ChatMessage = ({ message, isBot }: ChatMessageProps) => {
  return (
    <div className={cn(
      "flex w-full mb-4 items-start gap-2",
      isBot ? "justify-start" : "justify-end"
    )}>
      {isBot && (
        <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center flex-shrink-0">
          <Bot className="w-5 h-5 text-blue-600" />
        </div>
      )}
      <div className={cn(
        "max-w-[80%] rounded-xl px-4 py-2 shadow-sm",
        isBot ? "bg-white text-gray-800 border prose prose-sm max-w-none" : "bg-blue-500 text-white"
      )}>
        {isBot ? (
          <div className="markdown-content">
            <ReactMarkdown className="break-words prose prose-sm max-w-none">
              {message}
            </ReactMarkdown>
          </div>
        ) : (
          <p className="whitespace-pre-wrap break-words text-sm">{message}</p>
        )}
      </div>
      {!isBot && (
        <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center flex-shrink-0">
          <User className="w-5 h-5 text-white" />
        </div>
      )}
    </div>
  );
};

export default ChatMessage;
