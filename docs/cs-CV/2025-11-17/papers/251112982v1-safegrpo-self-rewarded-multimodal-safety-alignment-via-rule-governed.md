---
layout: default
title: SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization
---

# SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization

**arXiv**: [2511.12982v1](https://arxiv.org/abs/2511.12982) | [PDF](https://arxiv.org/pdf/2511.12982.pdf)

**作者**: Xuankun Rong, Wenke Huang, Tingfeng Wang, Daiguo Zhou, Bo Du, Mang Ye

---

## 💡 一句话要点

**提出SafeGRPO框架，通过规则治理策略优化解决多模态大模型组合安全风险**

**关键词**: `多模态安全对齐` `规则治理策略优化` `自奖励学习` `组合安全风险` `结构化推理`

## 📋 核心要点

1. 多模态大模型在文本-图像交互中易产生组合安全风险，即使输入无害也可能输出不安全语义
2. 方法将规则治理奖励构建融入GRPO，实现可解释的安全推理优化，基于SafeTag-VL-3K数据集进行结构化推理
3. 实验显示，在多种基准测试中显著提升多模态安全意识和组合鲁棒性，未牺牲通用能力

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have demonstrated impressive reasoning and instruction-following capabilities, yet their expanded modality space introduces new compositional safety risks that emerge from complex text-image interactions. Such cross-modal couplings can produce unsafe semantics even when individual inputs are benign, exposing the fragile safety awareness of current MLLMs. While recent works enhance safety by guiding models to reason about potential risks, unregulated reasoning traces may compromise alignment; although Group Relative Policy Optimization (GRPO) offers self-rewarded refinement without human supervision, it lacks verifiable signals for reasoning safety. To address this, we propose SafeGRPO a self-rewarded multimodal safety alignment framework that integrates rule-governed reward construction into GRPO, enabling interpretable and verifiable optimization of reasoning safety. Built upon the constructed SafeTag-VL-3K dataset with explicit visual, textual, and combined safety tags, SafeGRPO performs step-guided safety thinking to enforce structured reasoning and behavior alignment, substantially improving multimodal safety awareness, compositional robustness, and reasoning stability across diverse benchmarks without sacrificing general capabilities.

