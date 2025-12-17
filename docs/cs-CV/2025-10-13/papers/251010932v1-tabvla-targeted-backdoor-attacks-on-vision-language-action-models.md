---
layout: default
title: TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models
---

# TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models

**arXiv**: [2510.10932v1](https://arxiv.org/abs/2510.10932) | [PDF](https://arxiv.org/pdf/2510.10932.pdf)

**作者**: Zonghuan Xu, Xiang Zheng, Xingjun Ma, Yu-Gang Jiang

---

## 💡 一句话要点

**提出TabVLA框架，针对视觉-语言-动作模型进行目标后门攻击**

**关键词**: `后门攻击` `视觉-语言-动作模型` `黑盒微调` `中毒数据生成` `目标攻击` `安全威胁`

## 📋 核心要点

1. 核心问题：VLA模型易受目标后门攻击，可能导致系统故障或物理伤害
2. 方法要点：通过黑盒微调优化中毒数据生成，支持输入流编辑和场景内触发
3. 实验或效果：在OpenVLA-7B上验证，视觉通道为主要攻击面，攻击成功率高且鲁棒

## 📄 摘要（原文）

> With the growing deployment of Vision-Language-Action (VLA) models in
> real-world embodied AI systems, their increasing vulnerability to backdoor
> attacks poses a serious safety threat. A backdoored VLA agent can be covertly
> triggered by a pre-injected backdoor to execute adversarial actions,
> potentially causing system failures or even physical harm. Although backdoor
> attacks on VLA models have been explored, prior work has focused only on
> untargeted attacks, leaving the more practically threatening scenario of
> targeted manipulation unexamined. In this paper, we study targeted backdoor
> attacks on VLA models and introduce TabVLA, a novel framework that enables such
> attacks via black-box fine-tuning. TabVLA explores two deployment-relevant
> inference-time threat models: input-stream editing and in-scene triggering. It
> formulates poisoned data generation as an optimization problem to improve
> attack effectivess. Experiments with OpenVLA-7B on the LIBERO benchmark reveal
> that the vision channel is the principal attack surface: targeted backdoors
> succeed with minimal poisoning, remain robust across variations in trigger
> design, and are degraded only by positional mismatches between fine-tuning and
> inference triggers. We also investigate a potential detection-based defense
> against TabVLA, which reconstructs latent visual triggers from the input stream
> to flag activation-conditioned backdoor samples. Our work highlights the
> vulnerability of VLA models to targeted backdoor manipulation and underscores
> the need for more advanced defenses.

