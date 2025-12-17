---
layout: default
title: UniSER: A Foundation Model for Unified Soft Effects Removal
---

# UniSER: A Foundation Model for Unified Soft Effects Removal

**arXiv**: [2511.14183v1](https://arxiv.org/abs/2511.14183) | [PDF](https://arxiv.org/pdf/2511.14183.pdf)

**作者**: Jingdong Zhang, Lingzhi Zhang, Qing Liu, Mang Tik Chiu, Connelly Barnes, Yizhou Wang, Haoran You, Xiaoyang Liu, Yuqian Zhou, Zhe Lin, Eli Shechtman, Sohrab Amirghodsi, Xin Li, Wenping Wang, Xiaohang Zhan

---

## 💡 一句话要点

**提出UniSER基础模型以统一去除图像软效应**

**关键词**: `软效应去除` `基础模型` `扩散变换器` `图像恢复` `数据集构建`

## 📋 核心要点

1. 核心问题：图像常受镜头光晕、雾霾等软效应影响，现有模型缺乏统一处理能力。
2. 方法要点：构建大规模数据集并微调Diffusion Transformer，集成掩码和强度控制。
3. 实验或效果：在真实场景中优于专业和通用模型，实现高保真恢复。

## 📄 摘要（原文）

> Digital images are often degraded by soft effects such as lens flare, haze, shadows, and reflections, which reduce aesthetics even though the underlying pixels remain partially visible. The prevailing works address these degradations in isolation, developing highly specialized, specialist models that lack scalability and fail to exploit the shared underlying essences of these restoration problems. While specialist models are limited, recent large-scale pretrained generalist models offer powerful, text-driven image editing capabilities. while recent general-purpose systems (e.g., GPT-4o, Flux Kontext, Nano Banana) require detailed prompts and often fail to achieve robust removal on these fine-grained tasks or preserve identity of the scene. Leveraging the common essence of soft effects, i.e., semi-transparent occlusions, we introduce a foundational versatile model UniSER, capable of addressing diverse degradations caused by soft effects within a single framework. Our methodology centers on curating a massive 3.8M-pair dataset to ensure robustness and generalization, which includes novel, physically-plausible data to fill critical gaps in public benchmarks, and a tailored training pipeline that fine-tunes a Diffusion Transformer to learn robust restoration priors from this diverse data, integrating fine-grained mask and strength controls. This synergistic approach allows UniSER to significantly outperform both specialist and generalist models, achieving robust, high-fidelity restoration in the wild.

