---
layout: default
title: China Regional 3km Downscaling Based on Residual Corrective Diffusion Model
---

# China Regional 3km Downscaling Based on Residual Corrective Diffusion Model

**arXiv**: [2512.05377v1](https://arxiv.org/abs/2512.05377) | [PDF](https://arxiv.org/pdf/2512.05377.pdf)

**作者**: Honglu Sun, Hao Jing, Zhixiang Dai, Sa Xiao, Wei Xue, Jian Sun, Qifeng Lu

---

## 💡 一句话要点

**提出基于残差校正扩散模型的中国区域3公里降尺度方法，以提升高分辨率天气预报精度。**

**关键词**: `统计降尺度` `扩散模型` `天气预报` `高分辨率` `深度学习` `中国区域`

## 📋 核心要点

1. 核心问题：数值天气预报中高效生成高分辨率预报的挑战，需通过降尺度方法处理全球模型输出。
2. 方法要点：采用扩散模型CorrDiff框架，扩展区域并引入高层变量，添加全局残差连接以提高准确性。
3. 实验或效果：在中国区域应用，降尺度预报在目标变量的MAE上优于基准模型CMA-MESO，生成更真实的细节。

## 📄 摘要（原文）

> A fundamental challenge in numerical weather prediction is to efficiently produce high-resolution forecasts. A common solution is applying downscaling methods, which include dynamical downscaling and statistical downscaling, to the outputs of global models. This work focuses on statistical downscaling, which establishes statistical relationships between low-resolution and high-resolution historical data using statistical models. Deep learning has emerged as a powerful tool for this task, giving rise to various high-performance super-resolution models, which can be directly applied for downscaling, such as diffusion models and Generative Adversarial Networks. This work relies on a diffusion-based downscaling framework named CorrDiff. In contrast to the original work of CorrDiff, the region considered in this work is nearly 20 times larger, and we not only consider surface variables as in the original work, but also encounter high-level variables (six pressure levels) as target downscaling variables. In addition, a global residual connection is added to improve accuracy. In order to generate the 3km forecasts for the China region, we apply our trained models to the 25km global grid forecasts of CMA-GFS, an operational global model of the China Meteorological Administration (CMA), and SFF, a data-driven deep learning-based weather model developed from Spherical Fourier Neural Operators (SFNO). CMA-MESO, a high-resolution regional model, is chosen as the baseline model. The experimental results demonstrate that the forecasts downscaled by our method generally outperform the direct forecasts of CMA-MESO in terms of MAE for the target variables. Our forecasts of radar composite reflectivity show that CorrDiff, as a generative model, can generate fine-scale details that lead to more realistic predictions compared to the corresponding deterministic regression models.

