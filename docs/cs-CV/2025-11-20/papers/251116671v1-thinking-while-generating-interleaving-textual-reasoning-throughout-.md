---
layout: default
title: Thinking-while-Generating: Interleaving Textual Reasoning throughout Visual Generation
---

# Thinking-while-Generating: Interleaving Textual Reasoning throughout Visual Generation

**arXiv**: [2511.16671v1](https://arxiv.org/abs/2511.16671) | [PDF](https://arxiv.org/pdf/2511.16671.pdf)

**作者**: Ziyu Guo, Renrui Zhang, Hongyu Li, Manyuan Zhang, Xinyan Chen, Sifan Wang, Yan Feng, Peng Pei, Pheng-Ann Heng

---

## 💡 一句话要点

**提出Thinking-while-Generating框架，在视觉生成过程中交织文本推理以增强语义丰富性。**

**关键词**: `视觉生成` `文本推理` `多模态交互` `监督微调` `强化学习`

## 📋 核心要点

1. 现有方法在视觉生成前或后集成文本推理，缺乏生成过程中的实时多模态交互。
2. TwiG框架在视觉内容逐步生成时交织文本推理，指导局部区域并反思已合成内容。
3. 探索零样本提示、监督微调和强化学习策略，在TwiG-50K数据集上验证框架潜力。

## 📄 摘要（原文）

> Recent advances in visual generation have increasingly explored the integration of reasoning capabilities. They incorporate textual reasoning, i.e., think, either before (as pre-planning) or after (as post-refinement) the generation process, yet they lack on-the-fly multimodal interaction during the generation itself. In this preliminary study, we introduce Thinking-while-Generating (TwiG), the first interleaved framework that enables co-evolving textual reasoning throughout the visual generation process. As visual content is progressively generating, textual reasoning is interleaved to both guide upcoming local regions and reflect on previously synthesized ones. This dynamic interplay produces more context-aware and semantically rich visual outputs. To unveil the potential of this framework, we investigate three candidate strategies, zero-shot prompting, supervised fine-tuning (SFT) on our curated TwiG-50K dataset, and reinforcement learning (RL) via a customized TwiG-GRPO strategy, each offering unique insights into the dynamics of interleaved reasoning. We hope this work inspires further research into interleaving textual reasoning for enhanced visual generation. Code will be released at: https://github.com/ZiyuGuo99/Thinking-while-Generating.

