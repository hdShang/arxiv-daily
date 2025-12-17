---
layout: default
title: Synset Signset Germany: a Synthetic Dataset for German Traffic Sign Recognition
---

# Synset Signset Germany: a Synthetic Dataset for German Traffic Sign Recognition

**arXiv**: [2512.05936v1](https://arxiv.org/abs/2512.05936) | [PDF](https://arxiv.org/pdf/2512.05936.pdf)

**作者**: Anne Sielemann, Lena Loercher, Max-Lion Schumacher, Stefan Wolf, Masoud Roschani, Jens Ziehn

---

## 💡 一句话要点

**提出合成数据集Synset Signset Germany，结合数据驱动与解析建模以增强德国交通标志识别**

**关键词**: `合成数据集` `交通标志识别` `GAN纹理生成` `解析渲染` `可解释AI` `鲁棒性测试`

## 📋 核心要点

1. 核心问题：德国交通标志识别数据稀缺，尤其新发布标志，影响模型训练与测试。
2. 方法要点：使用GAN生成纹理模拟污损，结合解析渲染实现物理正确光照，支持参数化场景调制。
3. 实验或效果：评估数据集在真实基准GTSRB上的真实度，并与先进合成数据集CATERED比较，展示在XAI和鲁棒性测试中的应用潜力。

## 📄 摘要（原文）

> In this paper, we present a synthesis pipeline and dataset for training / testing data in the task of traffic sign recognition that combines the advantages of data-driven and analytical modeling: GAN-based texture generation enables data-driven dirt and wear artifacts, rendering unique and realistic traffic sign surfaces, while the analytical scene modulation achieves physically correct lighting and allows detailed parameterization. In particular, the latter opens up applications in the context of explainable AI (XAI) and robustness tests due to the possibility of evaluating the sensitivity to parameter changes, which we demonstrate with experiments. Our resulting synthetic traffic sign recognition dataset Synset Signset Germany contains a total of 105500 images of 211 different German traffic sign classes, including newly published (2020) and thus comparatively rare traffic signs. In addition to a mask and a segmentation image, we also provide extensive metadata including the stochastically selected environment and imaging effect parameters for each image. We evaluate the degree of realism of Synset Signset Germany on the real-world German Traffic Sign Recognition Benchmark (GTSRB) and in comparison to CATERED, a state-of-the-art synthetic traffic sign recognition dataset.

