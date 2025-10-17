# 🎨 UI Reference Guide - SOAR Frontend

## Visual Layout Reference

### 1. Homepage - Organization Cards (`index.html`)

```
┌────────────────────────────────────────────────────────────────┐
│  SOAR Logo   [🔔]  👤 Username  [Logout]                      │
└────────────────────────────────────────────────────────────────┘

    Welcome back, Username! 👋
    Here are the organizations you've joined

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│    [Academic]    │  │    [Sports]      │  │   [Community]    │
│                  │  │                  │  │                  │
│       🎓         │  │       ⚽         │  │       🤝         │
│                  │  │                  │  │                  │
│  Computer Sci    │  │  Basketball      │  │  Student Govt    │
│   Society        │  │   Team           │  │  Association     │
│                  │  │                  │  │                  │
│  Join us for     │  │  Play and        │  │  Leading the     │
│  exciting...     │  │  compete...      │  │  student body    │
│                  │  │                  │  │                  │
│  👥 128 members  │  │  👥 45 members   │  │  👥 89 members   │
│                  │  │                  │  │                  │
│  View Org →      │  │  View Org →      │  │  View Org →      │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

---

### 2. Organization Dashboard (`orgpage.html`)

```
┌──────────────┬─────────────────────────────────────────────────┐
│              │  ☰  Organization Dashboard    [Org Profile]    │
│   SIDEBAR    │                               [Member Mgmt] 👤 │
│              ├─────────────────────────────────────────────────┤
│  🏠 Feed     │                                                 │
│  📅 Events   │  ┌──────────────────────────────────────────┐  │
│  📢 Announce │  │  Create Post                              │  │
│  👥 Members  │  │  What's on your mind?                     │  │
│  🖼️  Gallery │  │  ________________________________         │  │
│  ⚙️  Settings│  │                                           │  │
│              │  │  📷 🎥 😊                       [Post]     │  │
│              │  └──────────────────────────────────────────┘  │
│              │                                                 │
│  [Back Home] │  ┌──────────────────────────────────────────┐  │
│              │  │  👤 Organization Admin  • 2 hours ago     │  │
│              │  │                                           │  │
│              │  │  Exciting news! We're hosting our annual  │  │
│              │  │  tech conference next month...            │  │
│              │  │                                           │  │
│              │  │  ❤️ 24   💬 8   🔗 3                      │  │
│              │  └──────────────────────────────────────────┘  │
│              │                                                 │
│              │  ┌──────────────────────────────────────────┐  │
│              │  │  👤 Active Member  • 5 hours ago          │  │
│              │  │                                           │  │
│              │  │  Great meeting today! Looking forward     │  │
│              │  │  to collaborating...                      │  │
│              │  │                                           │  │
│              │  │  ❤️ 15   💬 5   🔗 1                      │  │
│              │  └──────────────────────────────────────────┘  │
└──────────────┴─────────────────────────────────────────────────┘
```

---

### 3. Organization Profile (`organization_profile.html`)

```
┌──────────────┬─────────────────────────────────────────────────┐
│              │  ☰  Organization Profile    [Member Mgmt] 👤    │
│   SIDEBAR    ├─────────────────────────────────────────────────┤
│              │                                                 │
│  🏠 Feed     │  ┌─────────────────────────────────────────┐   │
│  📅 Events   │  │         🎓                              │   │
│  📢 Announce │  │   Computer Science Society              │   │
│  👥 Members  │  │   Promoting CS education...             │   │
│  🖼️  Gallery │  │                                         │   │
│  ⚙️  Settings│  │   👥 128 members  📅 Created Sep 2018   │   │
│  (active)    │  └─────────────────────────────────────────┘   │
│              │                                                 │
│  [Back Home] │  Organization Information                       │
│              │  ┌─────────────────────────────────────────┐   │
│              │  │  Organization Name *                    │   │
│              │  │  [Computer Science Society]             │   │
│              │  │                                         │   │
│              │  │  Adviser                                │   │
│              │  │  [Dr. Smith]            (read-only)     │   │
│              │  │                                         │   │
│              │  │  Description                            │   │
│              │  │  [___________________________]          │   │
│              │  │  [___________________________]          │   │
│              │  │                                         │   │
│              │  │  Organization Logo                      │   │
│              │  │  [Choose File]                          │   │
│              │  │                                         │   │
│              │  │           [Cancel]  [💾 Save Changes]   │   │
│              │  └─────────────────────────────────────────┘   │
│              │                                                 │
│              │  Additional Settings                            │
│              │  ┌─────────────────────────────────────────┐   │
│              │  │  Public Profile                    [🔘]  │   │
│              │  │  Allow Join Requests               [🔘]  │   │
│              │  │  Email Notifications               [ ]   │   │
│              │  └─────────────────────────────────────────┘   │
└──────────────┴─────────────────────────────────────────────────┘
```

---

### 4. Member Management (`membermanagement.html`)

```
┌──────────────┬─────────────────────────────────────────────────┐
│              │  ☰  Member Management        [Org Profile] 👤   │
│   SIDEBAR    ├─────────────────────────────────────────────────┤
│              │                                                 │
│  🏠 Feed     │  Add New Member                                 │
│  📅 Events   │  ┌────────────┬──────────┬──────────────────┐  │
│  📢 Announce │  │ Email *    │ Role *   │                  │  │
│  👥 Members  │  │ [_______]  │ [Member▾]│  [➕ Add Member] │  │
│  (active)    │  └────────────┴──────────┴──────────────────┘  │
│  🖼️  Gallery │                                                 │
│  ⚙️  Settings│  Members                                        │
│              │  Manage your organization members...            │
│              │                                                 │
│  [Back Home] │  [🔍 Search...]                  📊 15 members  │
│              │  ┌─────────────────────────────────────────┐   │
│              │  │ Name     │ Role   │ Joined   │ Status  │   │
│              │  ├─────────────────────────────────────────┤   │
│              │  │ 👤 John  │[Leader]│ Jan 2023 │[Active] │✏️↑🗑️│
│              │  │    Doe   │        │          │         │   │
│              │  ├─────────────────────────────────────────┤   │
│              │  │ 👤 Jane  │[Officer│ Feb 2023 │[Active] │✏️↑🗑️│
│              │  │    Smith │        │          │         │   │
│              │  ├─────────────────────────────────────────┤   │
│              │  │ 👤 Bob   │[Member]│ Mar 2023 │[Pending]│✏️↑🗑️│
│              │  │    Wilson│        │          │         │   │
│              │  └─────────────────────────────────────────┘   │
│              │                                                 │
│              │  Showing 1 to 15 of 15 members  [<] [1] [>]    │
└──────────────┴─────────────────────────────────────────────────┘
```

---

## 🎨 Color Coding Reference

### Role Badges
- **Leader**: 🟣 Purple background (#f3e8ff)
- **Officer**: 🔵 Blue background (#dbeafe)
- **Member**: ⚪ Gray background (#f3f4f6)

### Status Badges
- **Active**: 🟢 Green (#d1fae5)
- **Pending**: 🟡 Yellow (#fef3c7)

### Type Badges (Organizations)
- **Academic**: 🔵 Blue
- **Sports**: 🟢 Green
- **Arts**: 🟣 Purple
- **Community**: 🟠 Orange

### Action Buttons
- **Primary**: 🔵 Blue (#3b82f6)
- **Success**: 🟢 Green (#10b981)
- **Danger**: 🔴 Red (#ef4444)
- **Neutral**: ⚪ Gray (#6b7280)

---

## 📱 Responsive Breakpoints

### Mobile (<640px)
```
┌──────────────────┐
│  ☰ SOAR Logo  👤│
├──────────────────┤
│                  │
│  Organization    │
│  Card (Full)     │
│                  │
├──────────────────┤
│                  │
│  Organization    │
│  Card (Full)     │
│                  │
└──────────────────┘
```

### Tablet (640px-768px)
```
┌───────────────────────────┐
│  ☰ SOAR Logo         👤   │
├───────────────────────────┤
│           │               │
│  Org Card │  Org Card     │
│           │               │
├───────────────────────────┤
│           │               │
│  Org Card │  Org Card     │
│           │               │
└───────────────────────────┘
```

### Desktop (≥768px)
```
┌─────────────────────────────────────────┐
│  SOAR Logo            🔔  👤 Username   │
├─────────────────────────────────────────┤
│         │         │         │           │
│ Org 1   │ Org 2   │ Org 3   │ Org 4     │
│         │         │         │           │
├─────────────────────────────────────────┤
│         │         │         │           │
│ Org 5   │ Org 6   │ Org 7   │ Org 8     │
│         │         │         │           │
└─────────────────────────────────────────┘
```

---

## 🖱️ Interactive Elements

### Hover States
- **Cards**: Lift up 8px with shadow
- **Buttons**: Darken by 10%
- **Links**: Underline appears
- **Sidebar Items**: Blue background

### Click States
- **Buttons**: Scale down slightly
- **Cards**: Navigate to new page
- **Toggle**: Smooth transition

### Focus States
- **Inputs**: Blue ring around border
- **Buttons**: Blue ring around element

---

## 🌈 Design System Summary

| Element | Style |
|---------|-------|
| **Primary Font** | Inter (300-800) |
| **Heading Font** | Inter Bold (700-800) |
| **Body Font** | Inter Regular (400) |
| **Border Radius** | 8px (standard), 12px (large) |
| **Shadow** | 0 2px 4px rgba(0,0,0,0.05) |
| **Transition** | 300ms ease |
| **Spacing** | 4px increments (Tailwind) |

---

*Use this reference when making design decisions or modifications*
