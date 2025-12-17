---
layout: default
title: On the Temporality for Sketch Representation Learning
---

# On the Temporality for Sketch Representation Learning

**arXiv**: [2512.04007v1](https://arxiv.org/abs/2512.04007) | [PDF](https://arxiv.org/pdf/2512.04007.pdf)

**作者**: Marcelo Isaias de Moraes Junior, Moacir Antonelli Ponti

---

## 💡 一句话要点

**探究时序性在草图表示学习中的真实作用，比较绝对与相对坐标及解码器性能**

**关键词**: `草图表示学习` `时序建模` `坐标编码` `解码器比较` `序列处理`

## 📋 核心要点

1. 核心问题：时序性对草图表示质量的影响及序列化处理的合理性
2. 方法要点：分析绝对与相对坐标编码，比较自回归与非自回归解码器
3. 实验或效果：绝对坐标优于相对坐标，非自回归解码器表现更佳，时序重要性依赖顺序与任务

## 📄 摘要（原文）

> Sketches are simple human hand-drawn abstractions of complex scenes and real-world objects. Although the field of sketch representation learning has advanced significantly, there is still a gap in understanding the true relevance of the temporal aspect to the quality of these representations. This work investigates whether it is indeed justifiable to treat sketches as sequences, as well as which internal orders play a more relevant role. The results indicate that, although the use of traditional positional encodings is valid for modeling sketches as sequences, absolute coordinates consistently outperform relative ones. Furthermore, non-autoregressive decoders outperform their autoregressive counterparts. Finally, the importance of temporality was shown to depend on both the order considered and the task evaluated.

