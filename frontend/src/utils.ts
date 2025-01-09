export function getInitialBGColour(initials: string) {
      const colors = [
        'bg-red-500',
        'bg-blue-500',
        'bg-green-500',
        'bg-yellow-500',
        'bg-indigo-500',
        'bg-orange-500',
        'bg-pink-500',
      ]
      try {
        if (initials.length === 0) {
          return colors[0]
        }
      } catch (e) {
        return colors[0]
      }
      const charCode = initials.charCodeAt(0)
      return colors[charCode % colors.length]
    }