---
layout: default
title: LongCat-Image Technical Report
---

# LongCat-Image Technical Report

**arXiv**: [2512.07584v1](https://arxiv.org/abs/2512.07584) | [PDF](https://arxiv.org/pdf/2512.07584.pdf)

**作者**: Meituan LongCat Team, Hanghang Ma, Haoxian Tan, Jiale Huang, Junqiang Wu, Jun-Yan He, Lishuai Gao, Songlin Xiao, Xiaoming Wei, Xiaoqi Ma, Xunliang Cai, Yayong Guan, Jie Hu

---

## 💡 一句话要点

**提出LongCat-Image开源双语图像生成基础模型，以解决多语言文本渲染、真实感、部署效率和开发者可访问性等核心挑战。**

**关键词**: `图像生成` `多语言文本渲染` `扩散模型` `开源生态系统` `图像编辑` `部署效率`

## 📋 核心要点

1. 通过预训练、中训练和SFT阶段的数据策展策略，结合RL阶段的奖励模型，实现卓越文本渲染和真实感，提升美学质量。
2. 在中文字符渲染上设定新行业标准，支持复杂罕见字符，覆盖率和准确性优于开源和商业方案。
3. 采用紧凑设计，核心扩散模型仅6B参数，确保低VRAM使用和快速推理，降低部署成本，并在图像编辑中实现SOTA结果。

## 📄 摘要（原文）

> We introduce LongCat-Image, a pioneering open-source and bilingual (Chinese-English) foundation model for image generation, designed to address core challenges in multilingual text rendering, photorealism, deployment efficiency, and developer accessibility prevalent in current leading models. 1) We achieve this through rigorous data curation strategies across the pre-training, mid-training, and SFT stages, complemented by the coordinated use of curated reward models during the RL phase. This strategy establishes the model as a new state-of-the-art (SOTA), delivering superior text-rendering capabilities and remarkable photorealism, and significantly enhancing aesthetic quality. 2) Notably, it sets a new industry standard for Chinese character rendering. By supporting even complex and rare characters, it outperforms both major open-source and commercial solutions in coverage, while also achieving superior accuracy. 3) The model achieves remarkable efficiency through its compact design. With a core diffusion model of only 6B parameters, it is significantly smaller than the nearly 20B or larger Mixture-of-Experts (MoE) architectures common in the field. This ensures minimal VRAM usage and rapid inference, significantly reducing deployment costs. Beyond generation, LongCat-Image also excels in image editing, achieving SOTA results on standard benchmarks with superior editing consistency compared to other open-source works. 4) To fully empower the community, we have established the most comprehensive open-source ecosystem to date. We are releasing not only multiple model versions for text-to-image and image editing, including checkpoints after mid-training and post-training stages, but also the entire toolchain of training procedure. We believe that the openness of LongCat-Image will provide robust support for developers and researchers, pushing the frontiers of visual content creation.

