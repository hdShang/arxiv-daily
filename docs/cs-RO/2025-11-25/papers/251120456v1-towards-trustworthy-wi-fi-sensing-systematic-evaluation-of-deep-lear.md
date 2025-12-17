---
layout: default
title: Towards Trustworthy Wi-Fi Sensing: Systematic Evaluation of Deep Learning Model Robustness to Adversarial Attacks
---

# Towards Trustworthy Wi-Fi Sensing: Systematic Evaluation of Deep Learning Model Robustness to Adversarial Attacks

**arXiv**: [2511.20456v1](https://arxiv.org/abs/2511.20456) | [PDF](https://arxiv.org/pdf/2511.20456.pdf)

**作者**: Shreevanth Krishnaa Gopalakrishnan, Stephen Hailes

---

## 💡 一句话要点

**系统评估Wi-Fi感知深度学习模型对抗攻击的鲁棒性，以提升可信赖性**

**关键词**: `Wi-Fi感知` `对抗攻击` `模型鲁棒性` `信道状态信息` `深度学习评估` `安全无线系统`

## 📋 核心要点

1. 核心问题：CSI深度学习模型易受对抗攻击，威胁无线感知安全与可靠性
2. 方法要点：建立评估框架，比较不同模型在多种威胁模型下的鲁棒性
3. 实验或效果：小模型鲁棒性差，物理可行扰动降低攻击成功率，对抗训练提升鲁棒性

## 📄 摘要（原文）

> Machine learning has become integral to Channel State Information (CSI)-based human sensing systems and is expected to power applications such as device-free activity recognition and identity detection in future cellular and Wi-Fi generations. However, these systems rely on models whose decisions can be subtly perturbed, raising concerns for security and reliability in ubiquitous sensing. Quantifying and understanding the robustness of such models, defined as their ability to maintain accurate predictions under adversarial perturbations, is therefore critical before wireless sensing can be safely deployed in real-world environments.
>   This work presents a systematic evaluation of the robustness of CSI deep learning models under diverse threat models (white-box, black-box/transfer, and universal perturbations) and varying degrees of attack realism. We establish a framework to compare compact temporal autoencoder models with larger deep architectures across three public datasets, quantifying how model scale, training regime, and physical constraints influence robustness. Our experiments show that smaller models, while efficient and equally performant on clean data, are markedly less robust. We further confirm that physically realizable signal-space perturbations, designed to be feasible in real wireless channels, significantly reduce attack success compared to unconstrained feature-space attacks. Adversarial training mitigates these vulnerabilities, improving mean robust accuracy with only moderate degradation in clean performance across both model classes. As wireless sensing advances towards reliable, cross-domain operation, these findings provide quantitative baselines for robustness estimation and inform design principles for secure and trustworthy human-centered sensing systems.

