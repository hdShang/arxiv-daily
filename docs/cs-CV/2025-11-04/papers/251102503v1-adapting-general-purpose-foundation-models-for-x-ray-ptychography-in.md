---
layout: default
title: Adapting General-Purpose Foundation Models for X-ray Ptychography in Low-Data Regimes
---

# Adapting General-Purpose Foundation Models for X-ray Ptychography in Low-Data Regimes

**arXiv**: [2511.02503v1](https://arxiv.org/abs/2511.02503) | [PDF](https://arxiv.org/pdf/2511.02503.pdf)

**作者**: Robinson Umeike, Neil Getty, Yin Xiangyu, Yi Jiang

---

## 💡 一句话要点

**提出PtychoBench基准，比较SFT与ICL策略在低数据X射线叠层成像中的任务依赖性优化**

**关键词**: `X射线叠层成像` `基础模型适应` `监督微调` `上下文学习` `多模态基准` `低数据学习`

## 📋 核心要点

1. 核心问题：通用基础模型在科学任务中适应策略不明确，尤其在数据稀缺场景。
2. 方法要点：引入多模态基准，系统比较监督微调与上下文学习策略。
3. 实验或效果：视觉任务SFT与ICL互补，文本任务ICL更优，提供AI科学应用框架。

## 📄 摘要（原文）

> The automation of workflows in advanced microscopy is a key goal where
> foundation models like Language Models (LLMs) and Vision-Language Models (VLMs)
> show great potential. However, adapting these general-purpose models for
> specialized scientific tasks is critical, and the optimal domain adaptation
> strategy is often unclear. To address this, we introduce PtychoBench, a new
> multi-modal, multi-task benchmark for ptychographic analysis. Using this
> benchmark, we systematically compare two specialization strategies: Supervised
> Fine-Tuning (SFT) and In-Context Learning (ICL). We evaluate these strategies
> on a visual artifact detection task with VLMs and a textual parameter
> recommendation task with LLMs in a data-scarce regime. Our findings reveal that
> the optimal specialization pathway is task-dependent. For the visual task, SFT
> and ICL are highly complementary, with a fine-tuned model guided by
> context-aware examples achieving the highest mean performance (Micro-F1 of
> 0.728). Conversely, for the textual task, ICL on a large base model is the
> superior strategy, reaching a peak Micro-F1 of 0.847 and outperforming a
> powerful "super-expert" SFT model (0-shot Micro-F1 of 0.839). We also confirm
> the superiority of context-aware prompting and identify a consistent contextual
> interference phenomenon in fine-tuned models. These results, benchmarked
> against strong baselines including GPT-4o and a DINOv3-based classifier, offer
> key observations for AI in science: the optimal specialization path in our
> benchmark is dependent on the task modality, offering a clear framework for
> developing more effective science-based agentic systems.

