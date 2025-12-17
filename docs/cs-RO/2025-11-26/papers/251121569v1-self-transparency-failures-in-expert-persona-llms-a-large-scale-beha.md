---
layout: default
title: Self-Transparency Failures in Expert-Persona LLMs: A Large-Scale Behavioral Audit
---

# Self-Transparency Failures in Expert-Persona LLMs: A Large-Scale Behavioral Audit

**arXiv**: [2511.21569v1](https://arxiv.org/abs/2511.21569) | [PDF](https://arxiv.org/pdf/2511.21569.pdf)

**作者**: Alex Diep

---

## 💡 一句话要点

**揭示专家角色LLM自我透明度失败，需行为设计与验证**

**关键词**: `语言模型透明度` `专家角色审计` `行为不一致` `推理优化影响` `贝叶斯验证`

## 📋 核心要点

1. 核心问题：LLM在专家角色中无法可靠披露AI身份，危害用户信任。
2. 方法要点：采用公共花园设计，审计16个模型在19200次试验中的行为。
3. 实验效果：披露率2.8%-73.6%，模型身份比参数数更能预测行为。

## 📄 摘要（原文）

> If a language model cannot reliably disclose its AI identity in expert contexts, users cannot trust its competence boundaries. This study examines self-transparency in models assigned professional personas within high-stakes domains where false expertise risks user harm. Using a common-garden design, sixteen open-weight models (4B--671B parameters) were audited across 19,200 trials. Models exhibited sharp domain-specific inconsistency: a Financial Advisor persona elicited 30.8% disclosure initially, while a Neurosurgeon persona elicited only 3.5%. This creates preconditions for a "Reverse Gell-Mann Amnesia" effect, where transparency in some domains leads users to overgeneralize trust to contexts where disclosure fails. Disclosure ranged from 2.8% to 73.6%, with a 14B model reaching 61.4% while a 70B produced just 4.1%. Model identity predicted behavior better than parameter count ($ΔR_{adj}^{2} = 0.359$ vs 0.018). Reasoning optimization actively suppressed self-transparency in some models, with reasoning variants showing up to 48.4% lower disclosure than base counterparts. Bayesian validation with Rogan--Gladen correction confirmed robustness to measurement error ($κ= 0.908$). These findings demonstrate transparency reflects training factors rather than scale. Organizations cannot assume safety properties transfer to deployment contexts, requiring deliberate behavior design and empirical verification.

