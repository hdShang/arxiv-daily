---
layout: default
title: Quantum-Classical Physics-Informed Neural Networks for Solving Reservoir Seepage Equations
---

# Quantum-Classical Physics-Informed Neural Networks for Solving Reservoir Seepage Equations

**arXiv**: [2512.03923v1](https://arxiv.org/abs/2512.03923) | [PDF](https://arxiv.org/pdf/2512.03923.pdf)

**作者**: Xiang Rao, Yina Liu, Yuxuan Shen

---

## 💡 一句话要点

**提出量子-经典物理信息神经网络以解决油藏渗流方程求解中的参数效率与非线性拟合瓶颈**

**关键词**: `量子-经典混合神经网络` `物理信息神经网络` `油藏渗流方程` `离散变量量子电路` `高维特征映射` `参数效率优化`

## 📋 核心要点

1. 传统数值方法与经典PINNs在油藏渗流PDE求解中面临计算成本高、参数效率低等挑战
2. 集成离散变量量子电路与经典网络，利用量子特性增强高维特征映射并嵌入物理约束
3. 在三种典型渗流模型中验证QCPINN，相比经典PINNs以更少参数实现高精度预测

## 📄 摘要（原文）

> Solving partial differential equations (PDEs) for reservoir seepage is critical for optimizing oil and gas field development and predicting production performance. Traditional numerical methods suffer from mesh-dependent errors and high computational costs, while classical Physics-Informed Neural Networks (PINNs) face bottlenecks in parameter efficiency, high-dimensional expression, and strong nonlinear fitting. To address these limitations, we propose a Discrete Variable (DV)-Circuit Quantum-Classical Physics-Informed Neural Network (QCPINN) and apply it to three typical reservoir seepage models for the first time: the pressure diffusion equation for heterogeneous single-phase flow, the nonlinear Buckley-Leverett (BL) equation for two-phase waterflooding, and the convection-diffusion equation for compositional flow considering adsorption. The QCPINN integrates classical preprocessing/postprocessing networks with a DV quantum core, leveraging quantum superposition and entanglement to enhance high-dimensional feature mapping while embedding physical constraints to ensure solution consistency. We test three quantum circuit topologies (Cascade, Cross-mesh, Alternate) and demonstrate through numerical experiments that QCPINNs achieve high prediction accuracy with fewer parameters than classical PINNs. Specifically, the Alternate topology outperforms others in heterogeneous single-phase flow and two-phase BL equation simulations, while the Cascade topology excels in compositional flow with convection-dispersion-adsorption coupling. Our work verifies the feasibility of QCPINN for reservoir engineering applications, bridging the gap between quantum computing research and industrial practice in oil and gas engineering.

