import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Card, CardContent } from '@/components/ui/card';
import { Marquee } from '@/components/ui/3d-testimonails';

// Boss Moto Expertz reviews data with valid high quality avatar images
const testimonials = [
  {
    name: 'Rajan Kumar',
    username: '@rajan_re',
    body: 'Boss Moto diagnosed a persistent oil leak on my Himalayan that 2 other garages failed to fix. Top class transparency!',
    img: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80',
    country: '🇮🇳 India',
  },
  {
    name: 'Arjun Patel',
    username: '@arjun_rx100',
    body: 'Got my Yamaha RX100 restored here. Chrome finish and engine note bring back 90s memories!',
    img: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80',
    country: '🇮🇳 India',
  },
  {
    name: 'Vikram Rao',
    username: '@vikram_ktm',
    body: 'ECU dyno tuning on my Duke 390 made a huge difference. Mid-range torque feels punchier and heat is lower!',
    img: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80',
    country: '🇮🇳 India',
  },
  {
    name: 'Sophia Chen',
    username: '@sophia_ninja',
    body: 'Suspension setup for track days was dialed in perfectly. Best superbike service studio in town!',
    img: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&auto=format&fit=crop&q=80',
    country: '🇸🇬 Singapore',
  },
  {
    name: 'Marco Rossi',
    username: '@marco_bmw',
    body: 'Quick turnaround on full liquid service & brake pad replacement for my S1000RR. Extremely professional.',
    img: 'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=150&auto=format&fit=crop&q=80',
    country: '🇮🇹 Italy',
  },
  {
    name: 'Lucas Dupont',
    username: '@lucas_tri',
    body: 'Custom cafe racer handlebar & exhaust install was top notch. Highly recommend Boss Moto Expertz!',
    img: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80',
    country: '🇫🇷 France',
  },
  {
    name: 'Haruto Sato',
    username: '@haru_r1',
    body: 'Restoration quality is world-class. Attention to detail on wiring and paint protection is unmatched.',
    img: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&auto=format&fit=crop&q=80',
    country: '🇯🇵 Japan',
  },
  {
    name: 'Emma Watson',
    username: '@emma_gt650',
    body: 'The twin-cylinder exhaust tuning sounds absolute music to the ears. Love the customer service!',
    img: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=80',
    country: '🇬🇧 UK',
  },
  {
    name: 'Carlos Gomez',
    username: '@carlos_scram',
    body: 'Spares availability, quick turnaround, and detailed diagnostic report provided. 5 stars overall!',
    img: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=150&auto=format&fit=crop&q=80',
    country: '🇪🇸 Spain',
  },
];

function TestimonialCard({ img, name, username, body, country }: (typeof testimonials)[number]) {
  return (
    <Card className="w-50">
      <CardContent>
        <div className="flex items-center gap-2.5">
          <Avatar className="size-9">
            <AvatarImage src={img} alt={name} />
            <AvatarFallback>{name[0]}</AvatarFallback>
          </Avatar>
          <div className="flex flex-col">
            <figcaption className="text-sm font-medium text-foreground flex items-center gap-1">
              {name} <span className="text-xs">{country}</span>
            </figcaption>
            <p className="text-xs font-medium text-muted-foreground">{username}</p>
          </div>
        </div>
        <blockquote className="mt-3 text-sm text-secondary-foreground">{body}</blockquote>
      </CardContent>
    </Card>
  );
}

export default function DemoOne() {
  return (
    <div className="border border-border rounded-lg relative flex h-96 w-full max-w-[800px] flex-row items-center justify-center overflow-hidden gap-1.5 [perspective:300px]">
      <div
        className="flex flex-row items-center gap-4"
        style={{
          transform:
            'translateX(-100px) translateY(0px) translateZ(-100px) rotateX(20deg) rotateY(-10deg) rotateZ(20deg)',
        }}
      >
        {/* Vertical Marquee (downwards) */}
        <Marquee vertical pauseOnHover repeat={3} className="[--duration:40s]">
          {testimonials.map((review) => (
            <TestimonialCard key={review.username} {...review} />
          ))}
        </Marquee>
        {/* Vertical Marquee (upwards) */}
        <Marquee vertical pauseOnHover reverse repeat={3} className="[--duration:40s]">
          {testimonials.map((review) => (
            <TestimonialCard key={review.username} {...review} />
          ))}
        </Marquee>
        {/* Vertical Marquee (upwards) */}
        <Marquee vertical pauseOnHover repeat={3} className="[--duration:40s]">
          {testimonials.map((review) => (
            <TestimonialCard key={review.username} {...review} />
          ))}
        </Marquee>
        {/* Vertical Marquee (upwards) */}
        <Marquee vertical pauseOnHover reverse repeat={3} className="[--duration:40s]">
          {testimonials.map((review) => (
            <TestimonialCard key={review.username} {...review} />
          ))}
        </Marquee>
        {/* Gradient overlays for vertical marquee */}
        <div className="pointer-events-none absolute inset-x-0 top-0 h-1/4 bg-gradient-to-b from-background"></div>
        <div className="pointer-events-none absolute inset-x-0 bottom-0 h-1/4 bg-gradient-to-t from-background"></div>
        <div className="pointer-events-none absolute inset-y-0 left-0 w-1/4 bg-gradient-to-r from-background"></div>
        <div className="pointer-events-none absolute inset-y-0 right-0 w-1/4 bg-gradient-to-l from-background"></div>
      </div>
    </div>
  );
}
