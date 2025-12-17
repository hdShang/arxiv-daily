---
layout: default
title: MIRA: Multimodal Iterative Reasoning Agent for Image Editing
---

# MIRA: Multimodal Iterative Reasoning Agent for Image Editing

**arXiv**: [2511.21087v1](https://arxiv.org/abs/2511.21087) | [PDF](https://arxiv.org/pdf/2511.21087.pdf)

**作者**: Ziyun Zeng, Hang Hua, Jiebo Luo

---

## 💡 一句话要点

**提出MIRA多模态迭代推理代理以解决指令引导图像编辑中的语义漂移问题**

**关键词**: `多模态推理` `迭代编辑` `指令引导图像编辑` `语义一致性` `视觉反馈`

## 📋 核心要点

1. 扩散模型难以准确解析复杂用户指令，导致编辑语义漂移或未达预期
2. MIRA通过感知-推理-行动循环迭代预测原子编辑指令，利用视觉反馈决策
3. 结合MIRA-Editing数据集和SFT+GRPO训练，显著提升语义一致性和感知质量

## 📄 摘要（原文）

> Instruction-guided image editing offers an intuitive way for users to edit images with natural language. However, diffusion-based editing models often struggle to accurately interpret complex user instructions, especially those involving compositional relationships, contextual cues, or referring expressions, leading to edits that drift semantically or fail to reflect the intended changes. We tackle this problem by proposing MIRA (Multimodal Iterative Reasoning Agent), a lightweight, plug-and-play multimodal reasoning agent that performs editing through an iterative perception-reasoning-action loop, effectively simulating multi-turn human-model interaction processes. Instead of issuing a single prompt or static plan, MIRA predicts atomic edit instructions step by step, using visual feedback to make its decisions. Our 150K multimodal tool-use dataset, MIRA-Editing, combined with a two-stage SFT + GRPO training pipeline, enables MIRA to perform reasoning and editing over complex editing instructions. When paired with open-source image editing models such as Flux.1-Kontext, Step1X-Edit, and Qwen-Image-Edit, MIRA significantly improves both semantic consistency and perceptual quality, achieving performance comparable to or exceeding proprietary systems such as GPT-Image and Nano-Banana.

