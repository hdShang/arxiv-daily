---
layout: default
title: FineXtrol: Controllable Motion Generation via Fine-Grained Text
---

# FineXtrol: Controllable Motion Generation via Fine-Grained Text

**arXiv**: [2511.18927v1](https://arxiv.org/abs/2511.18927) | [PDF](https://arxiv.org/pdf/2511.18927.pdf)

**作者**: Keming Shen, Bizhu Wu, Junliang Chen, Xiaoqin Wang, Linlin Shen

---

## 💡 一句话要点

**提出FineXtrol框架，通过细粒度文本控制解决运动生成中的精度和效率问题**

**关键词**: `运动生成` `细粒度文本控制` `分层对比学习` `时间感知信号` `计算效率`

## 📋 核心要点

1. 核心问题：现有方法细节错位、缺乏时间线索或计算成本高
2. 方法要点：使用时间感知细粒度文本信号，结合分层对比学习提升嵌入判别性
3. 实验或效果：定量结果强，定性分析显示灵活控制身体部位运动

## 📄 摘要（原文）

> Recent works have sought to enhance the controllability and precision of text-driven motion generation. Some approaches leverage large language models (LLMs) to produce more detailed texts, while others incorporate global 3D coordinate sequences as additional control signals. However, the former often introduces misaligned details and lacks explicit temporal cues, and the latter incurs significant computational cost when converting coordinates to standard motion representations. To address these issues, we propose FineXtrol, a novel control framework for efficient motion generation guided by temporally-aware, precise, user-friendly, and fine-grained textual control signals that describe specific body part movements over time. In support of this framework, we design a hierarchical contrastive learning module that encourages the text encoder to produce more discriminative embeddings for our novel control signals, thereby improving motion controllability. Quantitative results show that FineXtrol achieves strong performance in controllable motion generation, while qualitative analysis demonstrates its flexibility in directing specific body part movements.

