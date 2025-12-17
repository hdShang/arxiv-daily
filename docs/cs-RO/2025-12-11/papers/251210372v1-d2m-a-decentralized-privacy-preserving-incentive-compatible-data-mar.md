---
layout: default
title: D2M: A Decentralized, Privacy-Preserving, Incentive-Compatible Data Marketplace for Collaborative Learning
---

# D2M: A Decentralized, Privacy-Preserving, Incentive-Compatible Data Marketplace for Collaborative Learning

**arXiv**: [2512.10372v1](https://arxiv.org/abs/2512.10372) | [PDF](https://arxiv.org/pdf/2512.10372.pdf)

**作者**: Yash Srivastava, Shalin Jain, Sneha Awathare, Nitin Awathare

---

## 💡 一句话要点

**提出D2M去中心化数据市场，结合联邦学习与区块链，解决隐私保护与激励兼容问题。**

**关键词**: `去中心化数据市场` `隐私保护联邦学习` `区块链仲裁` `激励兼容机制` `拜占庭鲁棒性`

## 📋 核心要点

1. 核心问题：现有联邦学习依赖可信聚合器，区块链数据市场计算密集且激励不足。
2. 方法要点：集成联邦学习、区块链仲裁和经济激励，使用YODA协议和Corrected OSMD增强鲁棒性。
3. 实验或效果：在MNIST和Fashion-MNIST上达高精度，30%拜占庭节点下性能下降小于3%。

## 📄 摘要（原文）

> The rising demand for collaborative machine learning and data analytics calls for secure and decentralized data sharing frameworks that balance privacy, trust, and incentives. Existing approaches, including federated learning (FL) and blockchain-based data markets, fall short: FL often depends on trusted aggregators and lacks Byzantine robustness, while blockchain frameworks struggle with computation-intensive training and incentive integration.
>   We present \prot, a decentralized data marketplace that unifies federated learning, blockchain arbitration, and economic incentives into a single framework for privacy-preserving data sharing. \prot\ enables data buyers to submit bid-based requests via blockchain smart contracts, which manage auctions, escrow, and dispute resolution. Computationally intensive training is delegated to \cone\ (\uline{Co}mpute \uline{N}etwork for \uline{E}xecution), an off-chain distributed execution layer. To safeguard against adversarial behavior, \prot\ integrates a modified YODA protocol with exponentially growing execution sets for resilient consensus, and introduces Corrected OSMD to mitigate malicious or low-quality contributions from sellers. All protocols are incentive-compatible, and our game-theoretic analysis establishes honesty as the dominant strategy.
>   We implement \prot\ on Ethereum and evaluate it over benchmark datasets -- MNIST, Fashion-MNIST, and CIFAR-10 -- under varying adversarial settings. \prot\ achieves up to 99\% accuracy on MNIST and 90\% on Fashion-MNIST, with less than 3\% degradation up to 30\% Byzantine nodes, and 56\% accuracy on CIFAR-10 despite its complexity. Our results show that \prot\ ensures privacy, maintains robustness under adversarial conditions, and scales efficiently with the number of participants, making it a practical foundation for real-world decentralized data sharing.

