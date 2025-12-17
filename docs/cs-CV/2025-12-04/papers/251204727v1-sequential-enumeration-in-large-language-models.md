---
layout: default
title: Sequential Enumeration in Large Language Models
---

# Sequential Enumeration in Large Language Models

**arXiv**: [2512.04727v1](https://arxiv.org/abs/2512.04727) | [PDF](https://arxiv.org/pdf/2512.04727.pdf)

**作者**: Kuinan Hou, Marco Zorzi, Alberto Testolin

---

## 💡 一句话要点

**探究大语言模型在序列枚举任务中的计数能力与局限性**

**关键词**: `序列枚举` `大语言模型` `计数能力` `思维链` `神经符号差距` `离散符号处理`

## 📋 核心要点

1. 核心问题：大语言模型能否系统性地计数和生成离散符号序列，以弥合神经与符号方法的差距。
2. 方法要点：测试五种先进大语言模型，通过不同提示指令探索思维链在计数策略自发涌现中的作用。
3. 实验或效果：模型在明确提示下可计数，但无法自发进行，计数能力未随规模扩展而稳健提升。

## 📄 摘要（原文）

> Reliably counting and generating sequences of items remain a significant challenge for neural networks, including Large Language Models (LLMs). Indeed, although this capability is readily handled by rule-based symbolic systems based on serial computation, learning to systematically deploy counting procedures is difficult for neural models, which should acquire these skills through learning. Previous research has demonstrated that recurrent architectures can only approximately track and enumerate sequences of events, and it remains unclear whether modern deep learning systems, including LLMs, can deploy systematic counting procedures over sequences of discrete symbols. This paper aims to fill this gap by investigating the sequential enumeration abilities of five state-of-the-art LLMs, including proprietary, open-source, and reasoning models. We probe LLMs in sequential naming and production tasks involving lists of letters and words, adopting a variety of prompting instructions to explore the role of chain-of-thought in the spontaneous emerging of counting strategies. We also evaluate open-source models with the same architecture but increasing size to see whether the mastering of counting principles follows scaling laws, and we analyze the embedding dynamics during sequential enumeration to investigate the emergent encoding of numerosity. We find that some LLMs are indeed capable of deploying counting procedures when explicitly prompted to do so, but none of them spontaneously engage in counting when simply asked to enumerate the number of items in a sequence. Our results suggest that, despite their impressive emergent abilities, LLMs cannot yet robustly and systematically deploy counting procedures, highlighting a persistent gap between neural and symbolic approaches to compositional generalization.

