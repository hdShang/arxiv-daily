---
layout: default
title: Masks Can Be Distracting: On Context Comprehension in Diffusion Language Models
---

# Masks Can Be Distracting: On Context Comprehension in Diffusion Language Models

**arXiv**: [2511.21338v1](https://arxiv.org/abs/2511.21338) | [PDF](https://arxiv.org/pdf/2511.21338.pdf)

**作者**: Julianna Piskorz, Cristina Pinneri, Alvaro Correia, Motasem Alfarra, Risheek Garrepalli, Christos Louizos

---

## 💡 一句话要点

**提出掩码无关损失函数以提升掩码扩散语言模型的上下文理解鲁棒性**

**关键词**: `掩码扩散语言模型` `上下文理解` `位置偏见` `掩码干扰` `损失函数设计` `模型鲁棒性`

## 📋 核心要点

1. 掩码扩散语言模型存在位置偏见和掩码干扰问题，影响上下文理解
2. 引入掩码无关损失函数，使预测对附加掩码数量不变
3. 微调后显著减轻掩码干扰，提高模型鲁棒性

## 📄 摘要（原文）

> Masked Diffusion Language Models (MDLMs) have recently emerged as a promising alternative to Autoregressive Language Models (ARLMs), leveraging a denoising objective that, in principle, should enable more uniform context utilisation. In this work, we examine the context comprehension abilities of MDLMs and uncover two key limitations. First, despite their more global training objective and bidirectional attention mechanism, similarly to ARLMS, MDLMs exhibit a strong locality bias: performance is highly sensitive to the position of relevant information within the input, favouring local over distant context. Second, we show that appending a large number of mask tokens--required for generation--can significantly degrade context comprehension. Through systematic ablations, we find that these masks act as distractors, reducing the model's ability to process relevant information. To address this, we introduce a mask-agnostic loss function that encourages predictions to remain invariant to the number of appended masks. Fine-tuning with this objective substantially mitigates the distracting effect of masks, improving robustness of MDLMs. Overall, our findings reveal critical limitations of the current MDLM training paradigm and provide actionable insights for building diffusion-based language models with stronger context comprehension.

