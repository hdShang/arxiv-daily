---
layout: default
title: Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous Parking
---

# Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous Parking

**arXiv**: [2510.20335v1](https://arxiv.org/abs/2510.20335) | [PDF](https://arxiv.org/pdf/2510.20335.pdf)

**作者**: Zixuan Wu, Hengyuan Zhang, Ting-Hsuan Chen, Yuliang Guo, David Paz, Xinyu Huang, Liu Ren

---

## 💡 一句话要点

**提出Dino-Diffusion Parking以解决自动驾驶停车中的跨域鲁棒性问题**

**关键词**: `自动驾驶停车` `跨域鲁棒性` `视觉基础模型` `扩散规划` `零样本转移` `模拟到真实转移`

## 📋 核心要点

1. 核心问题：端到端方法在天气和光照等域偏移下鲁棒性不足
2. 方法要点：集成视觉基础模型与扩散规划，实现领域无关感知和运动规划
3. 实验或效果：零样本转移至对抗场景，停车成功率超90%，验证跨域性能提升

## 📄 摘要（原文）

> Parking is a critical pillar of driving safety. While recent end-to-end (E2E)
> approaches have achieved promising in-domain results, robustness under domain
> shifts (e.g., weather and lighting changes) remains a key challenge. Rather
> than relying on additional data, in this paper, we propose Dino-Diffusion
> Parking (DDP), a domain-agnostic autonomous parking pipeline that integrates
> visual foundation models with diffusion-based planning to enable generalized
> perception and robust motion planning under distribution shifts. We train our
> pipeline in CARLA at regular setting and transfer it to more adversarial
> settings in a zero-shot fashion. Our model consistently achieves a parking
> success rate above 90% across all tested out-of-distribution (OOD) scenarios,
> with ablation studies confirming that both the network architecture and
> algorithmic design significantly enhance cross-domain performance over existing
> baselines. Furthermore, testing in a 3D Gaussian splatting (3DGS) environment
> reconstructed from a real-world parking lot demonstrates promising sim-to-real
> transfer.

