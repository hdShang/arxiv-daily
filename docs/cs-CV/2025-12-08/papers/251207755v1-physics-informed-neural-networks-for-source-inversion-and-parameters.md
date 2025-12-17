---
layout: default
title: Physics-Informed Neural Networks for Source Inversion and Parameters Estimation in Atmospheric Dispersion
---

# Physics-Informed Neural Networks for Source Inversion and Parameters Estimation in Atmospheric Dispersion

**arXiv**: [2512.07755v1](https://arxiv.org/abs/2512.07755) | [PDF](https://arxiv.org/pdf/2512.07755.pdf)

**作者**: Brenda Anague, Bamdad Hosseini, Issa Karambal, Jean Medard Ngnotchouye

---

## 💡 一句话要点

**提出加权自适应PINN方法以解决大气扩散中源反演与参数估计的联合问题**

**关键词**: `物理信息神经网络` `源反演` `参数估计` `对流扩散方程` `加权自适应方法` `大气扩散`

## 📋 核心要点

1. 核心问题：从稀疏数据中同时估计排放源位置及未知速度与扩散参数，任务高度不适定
2. 方法要点：基于神经正切核的加权自适应PINN，将PDE作为约束耦合多个未知函数参数
3. 实验或效果：在2D/3D对流扩散方程上验证方法成功且对测量噪声鲁棒

## 📄 摘要（原文）

> Recent studies have shown the success of deep learning in solving forward and inverse problems in engineering and scientific computing domains, such as physics-informed neural networks (PINNs). In the fields of atmospheric science and environmental monitoring, estimating emission source locations is a central task that further relies on multiple model parameters that dictate velocity profiles and diffusion parameters. Estimating these parameters at the same time as emission sources from scarce data is a difficult task. In this work, we achieve this by leveraging the flexibility and generality of PINNs. We use a weighted adaptive method based on the neural tangent kernels to solve a source inversion problem with parameter estimation on the 2D and 3D advection-diffusion equations with unknown velocity and diffusion coefficients that may vary in space and time. Our proposed weighted adaptive method is presented as an extension of PINNs for forward PDE problems to a highly ill-posed source inversion and parameter estimation problem. The key idea behind our methodology is to attempt the joint recovery of the solution, the sources along with the unknown parameters, thereby using the underlying partial differential equation as a constraint that couples multiple unknown functional parameters, leading to more efficient use of the limited information in the measurements. We present various numerical experiments, using different types of measurements that model practical engineering systems, to show that our proposed method is indeed successful and robust to additional noise in the measurements.

