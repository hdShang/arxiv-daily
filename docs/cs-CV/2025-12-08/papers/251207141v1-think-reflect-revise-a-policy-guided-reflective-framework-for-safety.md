---
layout: default
title: Think-Reflect-Revise: A Policy-Guided Reflective Framework for Safety Alignment in Large Vision Language Models
---

# Think-Reflect-Revise: A Policy-Guided Reflective Framework for Safety Alignment in Large Vision Language Models

**arXiv**: [2512.07141v1](https://arxiv.org/abs/2512.07141) | [PDF](https://arxiv.org/pdf/2512.07141.pdf)

**作者**: Fenghua Weng, Chaochao Lu, Xia Hu, Wenqi Shao, Wenjie Wang

---

## 💡 一句话要点

**提出Think-Reflect-Revise框架以增强大型视觉语言模型的安全对齐能力**

**关键词**: `大型视觉语言模型` `安全对齐` `自我反思` `强化学习` `越狱攻击` `多模态推理`

## 📋 核心要点

1. 核心问题：单次推理范式易受上下文或视觉越狱攻击，可能忽略自身输出中的有害内容。
2. 方法要点：构建包含5000个示例的ReSafe数据集，通过三阶段训练（数据集微调、强化学习）引导模型进行策略指导的自我反思。
3. 实验或效果：在Qwen2.5-VL-7B上，安全响应率从42.8%提升至87.7%，同时保持通用基准性能稳定。

## 📄 摘要（原文）

> As multimodal reasoning improves the overall capabilities of Large Vision Language Models (LVLMs), recent studies have begun to explore safety-oriented reasoning, aiming to enhance safety awareness by analyzing potential safety risks during the reasoning process before generating the final response. Although such approaches improve safety awareness and interpretability, this single-pass think-then-answer paradigm remains vulnerable to contextual or visual jailbreak attacks. This reveals a critical flaw: single-pass reasoning may overlook explicit harmful content in its own output. Our key insight is to exploit this wasted signal through reflection, which can effectively leverage the malicious content revealed in the first-pass reasoning to enable genuine self-correction and prevent unsafe generations. Motivated by this, we propose Think-Reflect-Revise (TRR), a three-stage training framework designed to enhance the safety alignment of LVLMs through policy-guided self-reflection. We first build a Reflective Safety Reasoning (ReSafe) dataset with 5,000 examples that follow a think-reflect-revise process. We then fine-tune the target model using the ReSafe dataset to initialize reflective behavior, and finally reinforce policy-guided reflection through reinforcement learning. Experimental results show that TRR substantially improves the safety performance of LVLMs across both safety-awareness benchmarks and jailbreak attack evaluations, increasing the overall safe response rate from 42.8% to 87.7% on Qwen2.5-VL-7B, while preserving stable performance on general benchmarks such as MMMU and MMStar. The project page is available at https://think-reflect-revise.github.io/.

