---
layout: default
title: Disrupting Hierarchical Reasoning: Adversarial Protection for Geographic Privacy in Multimodal Reasoning Models
---

# Disrupting Hierarchical Reasoning: Adversarial Protection for Geographic Privacy in Multimodal Reasoning Models

**arXiv**: [2512.08503v1](https://arxiv.org/abs/2512.08503) | [PDF](https://arxiv.org/pdf/2512.08503.pdf)

**作者**: Jiaming Zhang, Che Wang, Yang Cao, Longtao Huang, Wei Yang Bryan Lim

---

## 💡 一句话要点

**提出ReasonBreak对抗框架，通过概念感知扰动保护多模态推理模型中的地理隐私**

**关键词**: `地理隐私保护` `对抗扰动` `多模态推理模型` `分层推理` `概念感知` `隐私数据集`

## 📋 核心要点

1. 多模态大推理模型通过分层思维链推理从个人图像推断精确地理位置，现有隐私保护技术无效
2. ReasonBreak利用概念感知扰动，针对推理链中的关键概念依赖，破坏分层推理过程
3. 在七种先进模型上评估，ReasonBreak在区域级保护提升14.4%，区块级保护近翻倍

## 📄 摘要（原文）

> Multi-modal large reasoning models (MLRMs) pose significant privacy risks by inferring precise geographic locations from personal images through hierarchical chain-of-thought reasoning. Existing privacy protection techniques, primarily designed for perception-based models, prove ineffective against MLRMs' sophisticated multi-step reasoning processes that analyze environmental cues. We introduce \textbf{ReasonBreak}, a novel adversarial framework specifically designed to disrupt hierarchical reasoning in MLRMs through concept-aware perturbations. Our approach is founded on the key insight that effective disruption of geographic reasoning requires perturbations aligned with conceptual hierarchies rather than uniform noise. ReasonBreak strategically targets critical conceptual dependencies within reasoning chains, generating perturbations that invalidate specific inference steps and cascade through subsequent reasoning stages. To facilitate this approach, we contribute \textbf{GeoPrivacy-6K}, a comprehensive dataset comprising 6,341 ultra-high-resolution images ($\geq$2K) with hierarchical concept annotations. Extensive evaluation across seven state-of-the-art MLRMs (including GPT-o3, GPT-5, Gemini 2.5 Pro) demonstrates ReasonBreak's superior effectiveness, achieving a 14.4\% improvement in tract-level protection (33.8\% vs 19.4\%) and nearly doubling block-level protection (33.5\% vs 16.8\%). This work establishes a new paradigm for privacy protection against reasoning-based threats.

