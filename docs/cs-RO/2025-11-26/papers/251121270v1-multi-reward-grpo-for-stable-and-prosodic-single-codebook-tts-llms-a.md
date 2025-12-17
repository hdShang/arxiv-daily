---
layout: default
title: Multi-Reward GRPO for Stable and Prosodic Single-Codebook TTS LLMs at Scale
---

# Multi-Reward GRPO for Stable and Prosodic Single-Codebook TTS LLMs at Scale

**arXiv**: [2511.21270v1](https://arxiv.org/abs/2511.21270) | [PDF](https://arxiv.org/pdf/2511.21270.pdf)

**作者**: Yicheng Zhong, Peiji Yang, Zhisheng Wang

---

## 💡 一句话要点

**提出多奖励GRPO框架以解决单码本TTS LLM的韵律不稳定问题**

**关键词**: `文本到语音合成` `强化学习优化` `单码本模型` `韵律对齐` `可扩展性分析` `流式架构`

## 📋 核心要点

1. 单码本TTS LLM存在韵律不稳定、说话人漂移和自然度下降问题
2. 采用多奖励GRPO优化策略，集成长度惩罚、熵正则化和LLM标注韵律对齐奖励
3. 实验显示方法提升韵律稳定性、说话人相似性和整体自然度，并验证可扩展性

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) have transformed text-to-speech (TTS) synthesis, inspiring autoregressive frameworks that represent speech as sequences of discrete codec tokens. Among them, single-codebook TTS LLMs have emerged as compact and streamable architectures that jointly model semantic and acoustic integration. However, despite their efficiency, these models often exhibit unstable prosody, speaker drift, and degraded naturalness. To address these issues, we propose a multi-reward Group Relative Policy Optimization (GRPO) framework that directly optimizes the token generation policy of single-codebook TTS LLMs. Beyond standard intelligibility and speaker similarity objectives, our design integrates three rule-based rewards: a length penalty for duration consistency, an entropy regularization reward for decoding stability, and an LLM-annotated prosody alignment reward that explicitly supervises rhythm. In this prosody reward, an external reasoning LLM predicts multiple plausible pause structures via in-context learning, providing a human-preference-aligned supervisory signal for GRPO training. To assess universality, we further attach a flow-matching (FM) decoder on top of the GRPO-optimized AR backbone and observe consistent additional gains, indicating that our reinforcement optimization enhances the intrinsic AR policy. We further conduct a scalability analysis across data sizes and model scales, revealing that the proposed method consistently enhances prosodic stability, speaker similarity, and overall speech naturalness in single-codebook TTS LLMs.

