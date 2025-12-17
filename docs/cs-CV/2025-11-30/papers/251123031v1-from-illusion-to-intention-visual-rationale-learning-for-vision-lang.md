---
layout: default
title: From Illusion to Intention: Visual Rationale Learning for Vision-Language Reasoning
---

# From Illusion to Intention: Visual Rationale Learning for Vision-Language Reasoning

**arXiv**: [2511.23031v1](https://arxiv.org/abs/2511.23031) | [PDF](https://arxiv.org/pdf/2511.23031.pdf)

**作者**: Changpeng Wang, Haozhe Wang, Xi Chen, Junhan Liu, Taofeng Xue, Chong Peng, Donglian Qi, Fangzhen Lin, Yunfeng Yan

---

## 💡 一句话要点

**提出视觉理性学习以解决视觉语言推理中视觉动作未有效接地的问题**

**关键词**: `视觉语言推理` `视觉理性化` `过程监督` `强化学习` `端到端训练` `可解释性`

## 📋 核心要点

1. 核心问题：现有模型依赖与上下文无关的视觉动作，导致推理未真正基于视觉证据，形成‘图像思考幻觉’
2. 方法要点：将视觉动作重构为核心推理原语，通过过程监督、目标对齐和细粒度信用分配实现端到端训练
3. 实验或效果：在感知、幻觉和推理基准上实现最先进结果，建立任务无关、过程接地的视觉理性化范式

## 📄 摘要（原文）

> Recent advances in vision-language reasoning underscore the importance of thinking with images, where models actively ground their reasoning in visual evidence. Yet, prevailing frameworks treat visual actions as optional tools, boosting metrics but leaving reasoning ungrounded and crops ineffective. This gap gives rise to the illusion of thinking with images: models seem visually grounded but rely on context-agnostic actions that neither refine perception nor guide reasoning toward correct answers. We address this problem by reframing visual actions as core reasoning primitives rather than optional tools, which we term visual rationalization, the visual analogue of textual Chain-of-Thought. Building on this insight, we propose Visual Rationale Learning (ViRL), an end-to-end paradigm that grounds training in the visual rationale itself. ViRL integrates (1) Process Supervision with ground-truth rationales, (2) Objective Alignment via step-level reward shaping, and (3) Fine-Grained Credit Assignment to distinguish correct, redundant, and erroneous actions. By ensuring each action contributes meaningfully to the reasoning chain, ViRL enables models to "get the right answer for the right visual reason". Trained purely with end-to-end RL, ViRL achieves state-of-the-art results across benchmarks spanning perception, hallucination, and reasoning. This work establishes visual rationalization as a task-agnostic, process-grounded paradigm for building transparent, verifiable, and trustworthy vision-language models.

