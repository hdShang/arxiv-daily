---
layout: default
title: Mitigating Self-Preference by Authorship Obfuscation
---

# Mitigating Self-Preference by Authorship Obfuscation

**arXiv**: [2512.05379v1](https://arxiv.org/abs/2512.05379) | [PDF](https://arxiv.org/pdf/2512.05379.pdf)

**作者**: Taslim Mahbub, Shi Feng

---

## 💡 一句话要点

**提出作者身份混淆方法以缓解语言模型评估中的自我偏好偏差**

**关键词**: `语言模型评估` `自我偏好偏差` `作者身份混淆` `黑盒扰动` `同义词替换` `评估公正性`

## 📋 核心要点

1. 核心问题：语言模型评估器存在自我偏好偏差，即偏好自身输出，影响评估公正性。
2. 方法要点：通过黑盒扰动（如同义词替换）混淆评估候选的作者身份，降低自我识别能力。
3. 实验或效果：简单扰动可减少自我偏好，但完全消除偏差仍具挑战性，因风格差异中性化后偏差可能恢复。

## 📄 摘要（原文）

> Language models (LMs) judges are widely used to evaluate the quality of LM outputs. Despite many advantages, LM judges display concerning biases that can impair their integrity in evaluations. One such bias is self-preference: LM judges preferring their own answers over those produced by other LMs or humans. The bias is hard to eliminate as frontier LM judges can distinguish their own outputs from those of others, even when the evaluation candidates are not labeled with their sources. In this paper, we investigate strategies to mitigate self-preference by reducing the LM judges' ability to recognize their own outputs. We apply black-box perturbations to evaluation candidates in pairwise comparison to obfuscate the authorship and reduce self-recognition. We find that perturbations as simple as synonym replacement for a few words predictably reduce self-preference. However, we also uncover fundamental challenges to eliminating the bias: when we extrapolate our perturbations to a more complete neutralization of stylistic differences between the evaluation candidates, self-preference recovers. Our findings suggest that self-recognition and self-preference can happen on many semantic levels, and complete mitigation remains challenging despite promising initial results.

