---
layout: default
title: Comprehensive Deployment-Oriented Assessment for Cross-Environment Generalization in Deep Learning-Based mmWave Radar Sensing
---

# Comprehensive Deployment-Oriented Assessment for Cross-Environment Generalization in Deep Learning-Based mmWave Radar Sensing

**arXiv**: [2512.13018v1](https://arxiv.org/abs/2512.13018) | [PDF](https://arxiv.org/pdf/2512.13018.pdf)

**作者**: Tomoya Tanaka, Tomonori Ikeda, Ryo Yonemoto

---

## 💡 一句话要点

**评估深度学习毫米波雷达感知的跨环境泛化技术，提出基于幅度预处理的实用部署方案。**

**关键词**: `毫米波雷达感知` `跨环境泛化` `深度学习部署` `幅度预处理` `迁移学习` `室内人员计数`

## 📋 核心要点

1. 核心问题：深度学习RF感知在空间变化下的部署泛化能力不足，影响实际应用。
2. 方法要点：系统评估幅度预处理、数据增强和迁移学习等多种泛化技术。
3. 实验或效果：幅度加权在跨环境中表现最佳，迁移学习在大空间偏移下效果显著。

## 📄 摘要（原文）

> This study presents the first comprehensive evaluation of spatial generalization techniques, which are essential for the practical deployment of deep learning-based radio-frequency (RF) sensing. Focusing on people counting in indoor environments using frequency-modulated continuous-wave (FMCW) multiple-input multiple-output (MIMO) radar, we systematically investigate a broad set of approaches, including amplitude-based statistical preprocessing (sigmoid weighting and threshold zeroing), frequency-domain filtering, autoencoder-based background suppression, data augmentation strategies, and transfer learning. Experimental results collected across two environments with different layouts demonstrate that sigmoid-based amplitude weighting consistently achieves superior cross-environment performance, yielding 50.1% and 55.2% reductions in root-mean-square error (RMSE) and mean absolute error (MAE), respectively, compared with baseline methods. Data augmentation provides additional though modest benefits, with improvements up to 8.8% in MAE. By contrast, transfer learning proves indispensable for large spatial shifts, achieving 82.1% and 91.3% reductions in RMSE and MAE, respectively, with 540 target-domain samples. Taken together, these findings establish a highly practical direction for developing radar sensing systems capable of maintaining robust accuracy under spatial variations by integrating deep learning models with amplitude-based preprocessing and efficient transfer learning.

