---
layout: default
title: From See to Shield: ML-Assisted Fine-Grained Access Control for Visual Data
---

# From See to Shield: ML-Assisted Fine-Grained Access Control for Visual Data

**arXiv**: [2510.19418v1](https://arxiv.org/abs/2510.19418) | [PDF](https://arxiv.org/pdf/2510.19418.pdf)

**作者**: Mete Harun Akcay, Buse Gul Atli, Siddharth Prakash Rao, Alexandros Bakas

---

## 💡 一句话要点

**提出基于机器学习的细粒度访问控制系统，以保护视觉数据中的敏感区域。**

**关键词**: `细粒度访问控制` `敏感区域检测` `混合加密` `视觉数据保护` `密钥管理` `策略执行`

## 📋 核心要点

1. 核心问题：大规模数据共享中敏感信息识别与保护困难，需支持多角色权限管理。
2. 方法要点：集成敏感区域自动检测、后校正、密钥管理和访问控制模块，采用混合加密方案。
3. 实验或效果：在视觉数据集上验证，提升检测性能，平均解密时间低于1秒，确保高效可扩展。

## 📄 摘要（原文）

> As the volume of stored data continues to grow, identifying and protecting
> sensitive information within large repositories becomes increasingly
> challenging, especially when shared with multiple users with different roles
> and permissions. This work presents a system architecture for trusted data
> sharing with policy-driven access control, enabling selective protection of
> sensitive regions while maintaining scalability. The proposed architecture
> integrates four core modules that combine automated detection of sensitive
> regions, post-correction, key management, and access control. Sensitive regions
> are secured using a hybrid scheme that employs symmetric encryption for
> efficiency and Attribute-Based Encryption for policy enforcement. The system
> supports efficient key distribution and isolates key storage to strengthen
> overall security. To demonstrate its applicability, we evaluate the system on
> visual datasets, where Privacy-Sensitive Objects in images are automatically
> detected, reassessed, and selectively encrypted prior to sharing in a data
> repository. Experimental results show that our system provides effective PSO
> detection, increases macro-averaged F1 score (5%) and mean Average Precision
> (10%), and maintains an average policy-enforced decryption time of less than 1
> second per image. These results demonstrate the effectiveness, efficiency and
> scalability of our proposed solution for fine-grained access control.

