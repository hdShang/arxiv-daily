---
layout: default
title: COGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers
---

# COGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers

**arXiv**: [2512.02318v1](https://arxiv.org/abs/2512.02318) | [PDF](https://arxiv.org/pdf/2512.02318.pdf)

**作者**: Junyu Wang, Changjia Zhu, Yuanbo Zhou, Lingyao Li, Xu He, Junjie Xiong

---

## 💡 一句话要点

**评估多模态大语言模型对视觉验证码的攻击能力并提出防御指南**

**关键词**: `多模态大语言模型` `验证码安全` `攻击评估` `防御指南` `提示工程` `推理分析`

## 📋 核心要点

1. 研究多模态大语言模型如何削弱视觉验证码的安全性，识别攻击面
2. 评估7个主流模型在18种真实验证码任务上的性能，分析提示工程影响
3. 基于模型推理轨迹分析成功/失败机制，为选择和强化验证码提供防御指南

## 📄 摘要（原文）

> This paper studies how multimodal large language models (MLLMs) undermine the security guarantees of visual CAPTCHA. We identify the attack surface where an adversary can cheaply automate CAPTCHA solving using off-the-shelf models. We evaluate 7 leading commercial and open-source MLLMs across 18 real-world CAPTCHA task types, measuring single-shot accuracy, success under limited retries, end-to-end latency, and per-solve cost. We further analyze the impact of task-specific prompt engineering and few-shot demonstrations on solver effectiveness. We reveal that MLLMs can reliably solve recognition-oriented and low-interaction CAPTCHA tasks at human-like cost and latency, whereas tasks requiring fine-grained localization, multi-step spatial reasoning, or cross-frame consistency remain significantly harder for current models. By examining the reasoning traces of such MLLMs, we investigate the underlying mechanisms of why models succeed/fail on specific CAPTCHA puzzles and use these insights to derive defense-oriented guidelines for selecting and strengthening CAPTCHA tasks. We conclude by discussing implications for platform operators deploying CAPTCHA as part of their abuse-mitigation pipeline.Code Availability (https://anonymous.4open.science/r/Captcha-465E/).

