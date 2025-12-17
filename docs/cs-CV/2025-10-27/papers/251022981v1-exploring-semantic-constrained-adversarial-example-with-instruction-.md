---
layout: default
title: Exploring Semantic-constrained Adversarial Example with Instruction Uncertainty Reduction
---

# Exploring Semantic-constrained Adversarial Example with Instruction Uncertainty Reduction

**arXiv**: [2510.22981v1](https://arxiv.org/abs/2510.22981) | [PDF](https://arxiv.org/pdf/2510.22981.pdf)

**作者**: Jin Hu, Jiakai Wang, Linna Jing, Haolin Li, Haodong Liu, Haotong Qin, Aishan Liu, Ke Xu, Xianglong Liu

---

## 💡 一句话要点

**提出多维度指令不确定性减少框架以提升语义约束对抗样本的攻击能力**

**关键词**: `语义约束对抗样本` `指令不确定性减少` `扩散模型攻击` `3D对抗生成` `转移攻击性能`

## 📋 核心要点

1. 核心问题：现有方法因指令语义不确定性（如指代多样性和描述不完整）导致攻击能力不足
2. 方法要点：通过残差驱动采样、上下文编码约束和语义抽象评估来减少不确定性
3. 实验或效果：广泛实验显示InSUR在转移攻击性能上优越，并首次实现无参考3D对抗样本生成

## 📄 摘要（原文）

> Recently, semantically constrained adversarial examples (SemanticAE), which
> are directly generated from natural language instructions, have become a
> promising avenue for future research due to their flexible attacking forms. To
> generate SemanticAEs, current methods fall short of satisfactory attacking
> ability as the key underlying factors of semantic uncertainty in human
> instructions, such as referring diversity, descriptive incompleteness, and
> boundary ambiguity, have not been fully investigated. To tackle the issues,
> this paper develops a multi-dimensional instruction uncertainty reduction
> (InSUR) framework to generate more satisfactory SemanticAE, i.e., transferable,
> adaptive, and effective. Specifically, in the dimension of the sampling method,
> we propose the residual-driven attacking direction stabilization to alleviate
> the unstable adversarial optimization caused by the diversity of language
> references. By coarsely predicting the language-guided sampling process, the
> optimization process will be stabilized by the designed ResAdv-DDIM sampler,
> therefore releasing the transferable and robust adversarial capability of
> multi-step diffusion models. In task modeling, we propose the context-encoded
> attacking scenario constraint to supplement the missing knowledge from
> incomplete human instructions. Guidance masking and renderer integration are
> proposed to regulate the constraints of 2D/3D SemanticAE, activating stronger
> scenario-adapted attacks. Moreover, in the dimension of generator evaluation,
> we propose the semantic-abstracted attacking evaluation enhancement by
> clarifying the evaluation boundary, facilitating the development of more
> effective SemanticAE generators. Extensive experiments demonstrate the
> superiority of the transfer attack performance of InSUR. Moreover, we realize
> the reference-free generation of semantically constrained 3D adversarial
> examples for the first time.

