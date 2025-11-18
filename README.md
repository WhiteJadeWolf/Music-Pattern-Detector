# 🎵 Music Pattern Detector  
### *Implementing Aho–Corasick for Musical Analysis*

---

## **Abstract**
This project applies **finite automata** to real-time musical pattern detection.  
By combining **Aho–Corasick multi-pattern search** with **MIDI event streams**, we can efficiently detect recurring motifs, chord fragments, or melodic signatures inside MIDI files.

The system:  
**MIDI Input → music21 Parser → Aho-Corasick Automaton → Matched Motifs + Key Context**

---

## **The Challenge**
Traditional string-search algorithms (e.g., KMP, naive search) are optimized for **single** pattern matching.  
Musical analysis often requires detecting **multiple motifs simultaneously**, such as:

- riff collections  
- melodic phrases  
- harmonic progressions across octaves  

Standard search becomes inefficient because each motif must be checked independently.  
Aho–Corasick solves this by **building a single automaton** that matches all patterns in one pass.

---

## **The Solution: Aho–Corasick Automaton**
The system uses two core steps:

### **1. Trie Construction**
All motifs are inserted as sequences (e.g., MIDI pitches, intervals).  
Each node represents a partial motif.

### **2. Failure Links**
Failure transitions allow the automaton to “fall back” efficiently when a motif diverges, enabling linear-time scanning across the entire stream.

We leverage the **`ahocorasick` Python module**, giving us a compact and efficient backend for pattern matching over note sequences.

---

## **Implementation Details**

### ✔ **Pattern Engine — `ahocorasick`**
- Stores motifs as integer sequences (MIDI pitch values / intervals).  
- Supports O(n) search over long streams.  
- Associates metadata (motif name, description, tags) with each terminal state.

### ✔ **MIDI Processing — `music21`**
Used for:

- Extracting note streams from `.mid` files  
- Detecting **key signatures**, **time signatures**, and **melodic lines**  
- Converting notes into searchable representations:
  - absolute pitch (60, 62, 64…)  
  - interval-based ( +2, +2, −1… )  
  - rhythm patterns (durations)

### ✔ **Visualizing the Automaton — Graphviz**
Graphviz renders:

- state machine nodes  
- transition edges  
- failure links (dashed)  
- terminal/match states (highlighted)

---
